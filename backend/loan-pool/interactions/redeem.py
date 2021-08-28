import json
from os import environ
import boto3
from decimal import Decimal
from utils import exception_handler, decode_username
from internal_lambda_invoke_utils import invoke_transfer_lambda
from dynamo_utils import get_available_for_redemption, create_transaction_receipt, process_redemption

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
    
    username = decode_username(event)
    
    # outstanding_contribution = get_available_for_redemption(username, pool_id)
        
    # if not outstanding_contribution or redemption_amount > outstanding_contribution:
    #     return {
    #         "statusCode": 400,
    #         "body": json.dumps({
    #             "message": "Insufficient amount for redemption"
    #         }),
    #         "headers": {'Access-Control-Allow-Origin': "*"}
    #     }
    
    # # invoke the transfer API 
    # data = {
    #     "amount": redemption_amount,
    #     "to": "USER",
    #     "username": username
    # }
    # trf_response = invoke_transfer_lambda(data)
    trf_response = {'statusCode':200}
    
    if trf_response['statusCode'] == 200:
        # Log the transaction 
        transaction_details = {
            "transaction_type": "CREDIT",
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
                "message": "success",
            }),
            "headers": {'Access-Control-Allow-Origin': "*"}
        }
    return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "Unable to redeem contribution"
            }),
            "headers": {'Access-Control-Allow-Origin': "*"}
        }

