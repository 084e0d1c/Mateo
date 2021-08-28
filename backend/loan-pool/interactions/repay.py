import json
from decimal import Decimal
from os import environ

import boto3
from dynamo_utils import create_transaction_receipt, process_repayment
from internal_lambda_invoke_utils import (invoke_check_balance_lambda,
                                          invoke_transfer_lambda)
from utils import decode_username, exception_handler


@exception_handler
def main(event, context):
    """
    User redeem from pool

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

    repayment_amount = Decimal(str(body['repayment_amount']))
    uid = body['uid']
    
    username = decode_username(event)
    
    # available_balance = invoke_check_balance_lambda({'username': username})
    
    # if available_balance < repayment_amount:
    #     return {
    #         "statusCode": 400,
    #         "body": json.dumps({"error": "Not enough funds available for repayment"}),
    #         "headers": {
    #             "Access-Control-Allow-Origin": "*"
    #         }
    #     }
    
    # # invoke the transfer API 
    # trf_data = {
    #     "amount": repayment_amount,
    #     "to": "MATEO",
    #     "username": username
    # }
    
    # response = invoke_transfer_lambda(trf_data)
    response = {'statusCode': 200} 
    
    if response['statusCode'] == 200:
        # Perform the repayment distribution to loaners
        repayment_details = {
            "amount": repayment_amount,
            "uid": uid,
            "username": username
        }
        pool_id = process_repayment(repayment_details)
        
        # Log the successful transaction
        transaction_details = {
            "transaction_type": "DEBIT",
            "amount": repayment_amount,
            "pool_id": pool_id,
            "username": username
        }
        create_transaction_receipt(transaction_details)
        
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
                "message": "fail",
            }),
            "headers": {'Access-Control-Allow-Origin': "*"}
    }
        
        

