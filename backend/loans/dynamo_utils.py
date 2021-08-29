import json
import time
import uuid
from datetime import datetime
from decimal import Decimal
from os import environ

import boto3

from internal_lambda_invoke_utils import invoke_transfer_lambda, invoke_compute_credit_metric_lambda
from utils import CreditRating

dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
transaction_table = dynamodb.Table(environ.get('TRANSACTION_HISTORY_DATABASE_NAME'))
pool_table = dynamodb.Table(environ.get('POOL_DATABASE_NAME'))
loan_table = dynamodb.Table(environ.get('LOAN_DATABASE_NAME'))
uid_table = dynamodb.Table(environ.get('USER_TRANSACTION_DATABASE_NAME'))

# ---------------
# This file serves as a collection of helper functions for 
# interacting with dynamoDB, rather than having 1 lambda function
# to handle all the CRUD operations.
# ---------------

# ---------------
# Get pools, get one pools utils
# ---------------
def scan_all_pools(username):
    all_pools = pool_table.scan()['Items']
    
    user_detail = loan_table.get_item(Key={"username": username})['Item']
    
    for pool_detail in all_pools:
        # By default cannot loan unless credit passes
        pool_detail['loan'] = False
        
        # By default can't deposit if you have an existing loan
        pool_detail['deposit'] = True
        
        # Business Logic: Check if eligible for loan
        if CreditRating[user_detail['credit_rating']] >= CreditRating[pool_detail['credit_rating_requirement']]:
            pool_detail['loan'] = True
            pool_detail['max_loan_amount'] = user_detail['max_loan_amount'] - user_detail['outstanding_loan_amount']

        if user_detail['outstanding_loan_amount'] > 0:
            pool_detail['deposit'] = False
        
        # Mask the contribution from requestors
        del pool_detail['contribution_distribution']
        
        # Min the max loan to either pool balance or user limit
        pool_detail['max_loan_amount'] = min(pool_detail['max_loan_amount'], pool_detail['available_amount'])
        
    return all_pools

def check_pool_eligibility(username, pool_id):
    user_detail = loan_table.get_item(Key={"username": username})['Item']
    
    # Get pool details
    pool_detail = pool_table.get_item(Key={'pool_id':pool_id})['Item']
    
    # By default cannot loan unless credit passes
    pool_detail['loan'] = False
    
    # By default can't deposit if you have an existing loan
    pool_detail['deposit'] = True
    
    # Business Logic: Check if eligible for loan
    if CreditRating[user_detail['credit_rating']] >= CreditRating[pool_detail['credit_rating_requirement']]:
        pool_detail['loan'] = True
        pool_detail['max_loan_amount'] = user_detail['max_loan_amount'] - user_detail['outstanding_loan_amount']

    if user_detail['outstanding_loan_amount'] > 0:
        pool_detail['deposit'] = False
    
    # Mask the contribution from requestors
    del pool_detail['contribution_distribution']
    return pool_detail
    
# ---------------
# General utils
# ---------------
def update_user_transaction_uid_mapping(uid, username):
    
    uid_detail = uid_table.get_item(Key={'username': username})['Item']
    uid_detail['uid'] += f",{uid}"
    uid_table.put_item(Item=uid_detail)
    
def create_transaction_receipt(transaction_details):
    
    uid = uuid.uuid4()
    update_user_transaction_uid_mapping(uid, transaction_details['username'])
    transaction_details['uid'] = str(uid)
    transaction_details['datetime'] = Decimal(datetime.timestamp(datetime.now())*1000)
    transaction_details['amount'] = transaction_details['amount']
    transaction_table.put_item(Item=transaction_details)

def existing_outstanding_loans(username):
    return loan_table.get_item(Key={'username':username})['Item']['outstanding_loan_amount']

def update_bank_balance(username, bank_balance):
    user_details = loan_table.get_item(Key={'username':username})['Item']
    user_details['bank_balance'] = bank_balance
    loan_table.put_item(Item=user_details)
    invoke_compute_credit_metric_lambda({'username':username})
    
def get_pool_credit_rating(pool_id):
    return pool_table.get_item(Key={'pool_id': pool_id})['Item']['credit_rating_requirement']

# ---------------
# Deposit related utils
# ---------------

# Deposit update amount to pool
def update_user_pool_contribution(pool_id, amount, username):
    
    # Update pool database
    pool_item = pool_table.get_item(Key={'pool_id': pool_id})['Item']
    pool_item['contribution_distribution'][username] = pool_item['contribution_distribution'].get(username, 0) + amount
    pool_item['available_amount'] += amount
    pool_table.put_item(Item=pool_item)
    
    # Update user loan database
    user_details = loan_table.get_item(Key={'username': username})['Item']
    if pool_id in user_details['deposits_to_pools']:
        user_details['deposits_to_pools'][pool_id]['available'] += amount
        user_details['deposits_to_pools'][pool_id]['initial_deposit'] += amount
    else:
        user_details['deposits_to_pools'][pool_id] = {'available': amount, 
                                                      'in_loan': 0,
                                                      "initial_deposit": amount,
                                                      "interest_reward": 0
                                                      }
    user_details['loaning_toggle'] = True
    loan_table.put_item(Item=user_details)

# Cahnge Loan toggle to true / false
def update_loaning_toggle(username, state):
    user_details = loan_table.get_item(Key={'username': username})['Item']
    user_details['loaning_toggle'] = state
    loan_table.put_item(Item=user_details)

# ---------------
# Redemption related utils
# ---------------
def get_available_for_redemption(username, pool_id):
    user_to_pool_deposit_details = loan_table.get_item(Key={'username': username})['Item']['deposits_to_pools'][pool_id]
    total_withdrawable = user_to_pool_deposit_details['available'] + user_to_pool_deposit_details['interest_reward']
    return total_withdrawable

def process_redemption(username, redemption_amount, pool_id):
    
    # Update Pool to reduce the contribution and available amount
    pool_details = pool_table.get_item(Key={'pool_id': pool_id})['Item']
    
    pool_details['contribution_distribution'][username] -= redemption_amount
    pool_details['available_amount'] -= redemption_amount
    
    pool_table.put_item(Item=pool_details)
    
    # Update personal details
    user_details = loan_table.get_item(Key={'username': username})['Item']
    
    # Logic: Calculate how much of the redemption spills over to interest
    interest_redemption = redemption_amount - user_details['deposits_to_pools'][pool_id]['initial_deposit']
    if interest_redemption > Decimal("0"):
        adjusted_redemption_amount = user_details['deposits_to_pools'][pool_id]['initial_deposit'] - interest_redemption
        user_details['deposits_to_pools'][pool_id]['interest_reward'] -= interest_redemption
        user_details['deposits_to_pools'][pool_id]['initial_deposit'] -= adjusted_redemption_amount
    else:
        user_details['deposits_to_pools'][pool_id]['initial_deposit'] -= redemption_amount
    user_details['deposits_to_pools'][pool_id]['available'] -= redemption_amount
    
    loan_table.put_item(Item=user_details)
    
# ---------------
# Loan related utils
# ---------------

# Loans to check max amt
def available_to_loan_in_pool(pool_id):
    return pool_table.get_item(Key={'pool_id': pool_id})['Item']['available_amount']

def existing_deposit_check(username):
    user_contributions = loan_table.get_item(Key={'username': username})['Item']['deposits_to_pools']
    total = 0
    for pool in user_contributions:
        total += sum(user_contributions[pool].values())
    return total

def get_max_loan(username):
    user_details = loan_table.get_item(Key={'username':username})['Item']
    available_loan_amount = user_details['max_loan_amount'] - user_details['outstanding_loan_amount']
    return available_loan_amount, user_details['credit_rating']

def update_user_in_loan_and_pool_balance(pool_id, amount):
    
    # Update pool database
    pool_details = pool_table.get_item(Key={'pool_id': pool_id})['Item']
    
    # Generate the contribution distribution
    weight = amount / pool_details['available_amount']
    contribution_distribution = {k:v * weight for k, v in pool_details['contribution_distribution'].items()}
    
    pool_details['available_amount'] -= amount
    
    for username in contribution_distribution:
        # update the available and in loan
        user_details = loan_table.get_item(Key={'username': username})['Item']
        user_details['deposits_to_pools'][pool_id]['in_loan'] += contribution_distribution[username]
        user_details['deposits_to_pools'][pool_id]['available'] -= contribution_distribution[username]
        loan_table.put_item(Item=user_details)
    
    pool_table.put_item(Item=pool_details)
    
    return contribution_distribution

def process_loan(username, amount, pool_id):
    user_detail = loan_table.get_item(Key={'username': username})['Item']
    user_detail['outstanding_loan_amount'] += amount
    user_detail['max_loan_amount'] -= amount
    if pool_id in user_detail['loans_from_pools']:
        user_detail['loans_from_pools'][pool_id]['in_loan'] += amount
    else:
        user_detail['loans_from_pools'][pool_id] = {'in_loan': amount, 'repaid': Decimal("0"), 'interest_due': Decimal("0")}
    loan_table.put_item(Item=user_detail)
    
# ---------------
# Repayment related utils
# ---------------
def process_repayment(repayment_details):
    # Get the uid for the repayment to each indivdual that contributed
    transaction_detail = transaction_table.get_item(Key={'uid': repayment_details['uid']})['Item']
    pool_id = transaction_detail['pool_id']
    weight = repayment_details['amount'] / transaction_detail['remaining_repayment']
    for username, value in transaction_detail['contribution'].items():
        weighted_repayment = value * weight
        repay(username, weighted_repayment, transaction_detail['pool_id'])
        transaction_detail['contribution'] = {username: value - weighted_repayment}

    current_sys_time = str(datetime.timestamp(datetime.now())*1000)
    transaction_detail['repayment_hist'][current_sys_time] =  repayment_details['amount']
    transaction_detail['remaining_repayment'] -= repayment_details['amount']
    if transaction_detail['remaining_repayment'] == 0:
        transaction_detail['repaid'] = True
    
    amount_repaid = transaction_detail['amount'] - transaction_detail['remaining_repayment']
    transaction_detail["pct_completed"] = int(amount_repaid/transaction_detail['amount'] * 100)
    transaction_table.put_item(Item=transaction_detail)
    
    # Update Loan userbase
    user_detail = loan_table.get_item(Key={'username':repayment_details['username']})['Item']
    user_detail['outstanding_loan_amount'] -= repayment_details['amount']
    user_detail['max_loan_amount'] += repayment_details['amount']
    user_detail['loans_from_pools'][pool_id]['in_loan'] -= repayment_details['amount']
    if 'repaid' in user_detail['loans_from_pools'][pool_id]:
        user_detail['loans_from_pools'][pool_id]['repaid'] += repayment_details['amount']
    else:
        user_detail['loans_from_pools'][pool_id]['repaid'] = repayment_details['amount']
    
    # Update pool value to reflect the repayment amount
    pool_item = pool_table.get_item(Key={'pool_id': pool_id})['Item']
    pool_item['available_amount'] += repayment_details['amount']
    pool_table.put_item(Item=pool_item)
    
    # If user has repaid everything, we clear the thing altogether
    if user_detail['loans_from_pools'][pool_id]['in_loan'] <= Decimal("0"):
        del user_detail['loans_from_pools'][pool_id]
        
    loan_table.put_item(Item=user_detail)
    invoke_compute_credit_metric_lambda(username)
    return pool_id
    
def repay(username, amount, pool_id):
    user_detail = loan_table.get_item(Key={'username': username})['Item']
    
    user_detail['deposits_to_pools'][pool_id]['in_loan'] -= amount
    
    if user_detail['loaning_toggle'] == False:
        # initiate the bank xfer back to user
        trf_data = {
            "amount": amount,
            "to": "USER",
            "username": username
        }
        
        response = invoke_transfer_lambda(trf_data)
        user_detail['deposits_to_pools'][pool_id]['intial_deposit'] -= amount
        transaction_details = {
            "transaction_type": "Withdrawal",
            "amount": amount,
            "pool_id": pool_id,
            "username": username
        }
        create_transaction_receipt(transaction_details)
    else:
        # If user don't want to loan anymore, then available should not change
        user_detail['deposits_to_pools'][pool_id]['available'] += amount
    
    loan_table.put_item(Item=user_detail)

    