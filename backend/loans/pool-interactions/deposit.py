import simplejson as json
from decimal import Decimal
from os import environ

from dynamo_utils import (create_transaction_receipt,
                          update_user_pool_contribution,
                          existing_outstanding_loans)
from internal_lambda_invoke_utils import invoke_check_balance_lambda, invoke_transfer_lambda
from utils import decode_username, exception_handler

@exception_handler
def main(event, context):
    """
    User deposit to pool from their bank account via user transfer lambda

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

    deposit_amount = Decimal(str(body['deposit_amount']))
    pool_id = body['pool_id']
    username = decode_username(event)
    
    
    # Business Logic 1 : check if remaining balance is sufficient for the top up
    available_balance = invoke_check_balance_lambda(event)
    
    if available_balance < deposit_amount:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "You have insufficient funds available in the bank"}),
            "headers": {
                "Access-Control-Allow-Origin": "*"
            }
        }
    
    # Business Logic 2: Check if he has any existing loans, if so, then return error
    # Although frontend should prevent this from happening, if a user tries to invoke the API directly
    # We can prevent this here again
    if existing_outstanding_loans(username) > Decimal("0"):
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "You have an existing outstanding loan"}),
            "headers": {
                "Access-Control-Allow-Origin": "*"
            }
        }
    
    # Verbose: Now, the depositing user has NO existing loans, and has sufficient funds in the bank
    # Hence, we can proceed with the deposit
    
    # Invoke the transfer API 
    data = {
        "amount": deposit_amount,
        "to": "MATEO",
        "username": username
    }
    
    response = invoke_transfer_lambda(data)
    
    if response['statusCode'] == 200:
        # Successful transfer
        
        # Business Logic 3: 
        # 1 - Update pool to reflect user contribution
        # 2 - Update user profile to reflect the deposit
        # 3 - Log the transaction
        update_user_pool_contribution(pool_id, deposit_amount, username)
        
        # This is the logging part
        transaction_details = {
            "transaction_type": "Payment",
            "amount": deposit_amount,
            "pool_id": pool_id,
            "username": username
        }
        create_transaction_receipt(transaction_details)
    
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Successfully deposited into pool",
            }),
            "headers": {'Access-Control-Allow-Origin': "*"}
        }
    else:
        # Bank Transfer failed, return error
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "Sorry! There was an issue with the bank. Please try again soon.",
            }),
            "headers": {'Access-Control-Allow-Origin': "*"}
        }

