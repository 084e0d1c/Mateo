import json
from decimal import Decimal

from dynamo_utils import (create_transaction_receipt,
                          get_available_for_redemption, process_redemption)
from internal_lambda_invoke_utils import invoke_transfer_lambda
from utils import decode_username, exception_handler


@exception_handler
def main(event, context):
    """
    User redeem their original contribution from the pool.

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

    redemption_amount = Decimal(str(body['redemption_amount']))
    pool_id = body['pool_id']
    fees = Decimal(str(body['fees']))
    
    
    username = decode_username(event)
    
    # Business Logic 1: Check if user has sufficient withdrawable balance
    outstanding_contribution = get_available_for_redemption(username, pool_id)
    
    if not outstanding_contribution or (redemption_amount + fees) > outstanding_contribution:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "Insufficient amount for redemption"
            }),
            "headers": {'Access-Control-Allow-Origin': "*"}
        }
    
    # Business Logic 2: Initate the bank transfer for user
    # The remaining fees is kept in Mateo's bank account
    # The consolidation of revenue can be derived from the logs
    data = {
        "amount": redemption_amount - fees,
        "to": "USER",
        "username": username
    }
    trf_response = invoke_transfer_lambda(data)
    
    if trf_response['statusCode'] == 200:
        # Log the transaction 
        transaction_details = {
            "transaction_type": "Withdrawal",
            "amount": redemption_amount,
            "pool_id": pool_id,
            "username": username
        }
        create_transaction_receipt(transaction_details)
        
        # Update pool amount and loan
        process_redemption(username, redemption_amount, pool_id)

        return {
            "statusCode": "200",
            "body": json.dumps({
                "message": "Successfully redeemed from loan pool",
            }),
            "headers": {'Access-Control-Allow-Origin': "*"}
        }
    return {
            "statusCode": 400,
            "body": json.dumps({
               "message": "Sorry! There was an issue with the bank. Please try again soon."
            }),
            "headers": {'Access-Control-Allow-Origin': "*"}
        }

