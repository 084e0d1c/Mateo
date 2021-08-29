from decimal import Decimal

import simplejson as json
from dynamo_utils import (available_to_loan_in_pool,
                          create_transaction_receipt, existing_deposit_check,
                          get_max_loan, get_pool_credit_rating, process_loan,
                          update_user_in_loan_and_pool_balance)
from internal_lambda_invoke_utils import (invoke_check_balance_lambda,
                                          invoke_transfer_lambda)
from utils import CreditRating, decode_username, exception_handler


@exception_handler
def main(event, context):
    """
    User gets loan from loan pool by invoking the user transfer lambda.

    Args:
        event (dict): API Gateway Format,
        context (dict): API Gateway Format

    Returns:
        API Gateway Response (dict): {
            "statusCode": <>, 
            "body": <>, 
            "headers": <>
        }

    """
    
    body = json.loads(event['body'])

    loan_amount = Decimal(str(body['loan_amount']))
    pool_id = body['pool_id']
    fees = Decimal(str(body['fees']))
    username = decode_username(event)
    
    
    
    # Business Logic 1: Check with dynamo if the user has enough credit to take loan
    available_loan_amount, credit_rating = get_max_loan(username)
    pool_credit_rating = get_pool_credit_rating(pool_id)
    if loan_amount > available_loan_amount or CreditRating[credit_rating] < CreditRating[pool_credit_rating]:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "User has insufficient credit to take loan"
            }),
            "headers": {'Access-Control-Allow-Origin': "*"}
        }
    
    # -----------
    # NOTE: These should be handled by frontend, but we have it here to double check
    # ------------
    
    # Business Logic 2: Check if pool has sufficient credit to lend
    pool_availability = available_to_loan_in_pool(pool_id)
    if loan_amount > pool_availability:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "Pool does not have sufficient money to loan"
            }),
            "headers": {'Access-Control-Allow-Origin': "*"}
        }
    
    # Business Logic 3: Check if user has any existing deposits, if so, can't loan
    existing_deposits = existing_deposit_check(username)
    if existing_deposits > Decimal("0"):
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "User already has an existing deposit"
            }),
            "headers": {'Access-Control-Allow-Origin': "*"}
        }
            
    
    # invoke the transfer API 
    # The user will receive the loan amount less the feess
    data = {
        "amount": loan_amount - fees,
        "to": "USER",
        "username": username
    }
    
    response = invoke_transfer_lambda(data)
    
    if response['statusCode'] == 200:
        contribution_distribution = update_user_in_loan_and_pool_balance(pool_id, loan_amount)
        
        process_loan(username, loan_amount, pool_id)
        print('processed loan')
        # update to transaction history database
        transaction_details = {
            "transaction_type": "Withdrawal",
            "amount": loan_amount,
            "remaining_repayment": loan_amount,
            "fees": fees,
            "pool_id": pool_id,
            "repaid": False,
            "contribution": contribution_distribution,
            "repayment_hist": {},
            "pct_completed": 0,
            "username": username
        }
        
        create_transaction_receipt(transaction_details)
        print('recipet')
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Pool loan successfully obtained",
            }),
            "headers": {'Access-Control-Allow-Origin': "*"}
        }
    else:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "Sorry! There was an issue with the bank. Please try again soon."
            }),
            "headers": {'Access-Control-Allow-Origin': "*"}
        }

