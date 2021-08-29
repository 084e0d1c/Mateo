from os import environ

import boto3
import simplejson as json
from decimal import Decimal
from dynamo_utils import check_pool_eligibility
from utils import decode_username, exception_handler

dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
loan_table = dynamodb.Table(environ.get('LOAN_DATABASE_NAME'))

@exception_handler
def main(event, context):
    """
    Retrieve a list of a specific pool with business logic

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
    
    username = decode_username(event)
    
    user_profile = loan_table.get_item(Key={'username': username})['Item']
    
    # Pool Related
    # Deposit POV
    total_deposits =  sum([user_profile['deposits_to_pools'][pool_id]['initial_deposit'] for pool_id in user_profile['deposits_to_pools']])
    total_available =  sum([user_profile['deposits_to_pools'][pool_id]['available'] for pool_id in user_profile['deposits_to_pools']])
    
    # Loan POV
    total_pool_repaid = sum([user_profile['loans_from_pools'][pool_id]['repaid'] for pool_id in user_profile['loans_from_pools']])
    total_pool_outstanding = sum([user_profile['loans_from_pools'][pool_id]['in_loan'] for pool_id in user_profile['loans_from_pools']])
    
    user_profile['outstanding_inital_deposits'] = total_deposits
    user_profile['outstanding_available_withdraw'] = total_available
    
    # Bank Loan Related
    total_bank_loan_repaid = sum([user_profile['loans_from_banks'][loan_purpose]['amount_repaid'] for loan_purpose in user_profile['loans_from_banks']])
    total_bank_loan_outstanding = sum([user_profile['loans_from_banks'][loan_purpose]['amount_remaining'] for loan_purpose in user_profile['loans_from_banks']])
    
    # Compile all loans for UI Display
    total_loan_repaid = total_bank_loan_repaid + total_pool_repaid
    total_loan_outstanding = total_pool_outstanding + total_bank_loan_outstanding
    pct_repaid = (total_loan_repaid / (total_loan_outstanding+total_loan_repaid)) * 100
    
    user_profile['total_loan_oustanding'] = total_loan_outstanding
    user_profile['pct_repaid'] = pct_repaid
    return {
        "statusCode": "200",
        "body": json.dumps({
            "message": "success",
            "body": user_profile
        }),
        "headers": {'Access-Control-Allow-Origin': "*"}
    }

