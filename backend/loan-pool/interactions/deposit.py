import json
from os import environ

import boto3

from dynamo_utils import (create_transaction_receipt,
                          update_user_pool_contribution)
from utils import decode_username, exception_handler

lambda_client = boto3.client('lambda', region_name='ap-southeast-1')

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

    deposit_amount = body['deposit_amount']
    pool_id = body['pool_id']
    username = decode_username(event)
    
    # check if remaining balance is sufficient for the top up
    user_detail_arn = environ.get('USER_DETAIL_LAMBDA')
    user_detail_response = lambda_client.invoke(FunctionName=user_detail_arn, InvocationType='RequestResponse', Payload=json.dumps({"username": username}))
    user_detail_json = json.loads(user_detail_response)
    
    if user_detail_json['available_balance'] < deposit_amount:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Insufficient funds available"}),
            "headers": {
                "Access-Control-Allow-Origin": "*"
            }
        }
    
    # invoke the transfer API 
    data = {
        "amount": deposit_amount,
        "to": "MATEO",
        "username": username
    }
    
    user_trf_arn = environ.get('USER_TRANSFER_LAMBDA')
    response = lambda_client.invoke(FunctionName=user_trf_arn, InvocationType='RequestResponse', Payload=json.dumps(data))
    
    if response['statusCode'] == 200:
        # if the transfer was successful update the user loan database and pool db
        update_user_pool_contribution(pool_id, deposit_amount, username)
        
        # update to transaction history database
        transaction_details = {
            "transaction_type": "DEBIT",
            "amount": deposit_amount,
            "pool_id": pool_id,
            "username": username
        }
        create_transaction_receipt(transaction_details)
    
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "success",
            }),
            "headers": {'Access-Control-Allow-Origin': "*"}
        }
    else:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "deposit failed",
            }),
            "headers": {'Access-Control-Allow-Origin': "*"}
        }

