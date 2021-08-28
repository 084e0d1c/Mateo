import json
from decimal import Decimal
from os import environ

import boto3
import jwt
from dynamo_utils import (create_transaction_receipt, get_max_loan,
                          process_loan, update_user_in_loan_and_pool_balance)
from utils import decode_username, exception_handler

lambda_client = boto3.client('lambda', region_name='ap-southeast-1')

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
    username = decode_username(event)
    
    # # check with dynamo if the user has enough credit to take loan
    # available_loan_amount = get_max_loan(username)
    # if loan_amount > available_loan_amount:
    #     return {
    #         "statusCode": 400,
    #         "body": json.dumps({
    #             "message": "User has insufficient credit to take loan"
    #         }),
    #         "headers": {'Access-Control-Allow-Origin': "*"}
    #     }
    
    # # invoke the transfer API 
    # data = {
    #     "amount": loan_amount,
    #     "to": "USER",
    #     "username": username
    # }
    
    # user_trf_arn = environ.get('USER_TRANSFER_LAMBDA')
    # response = lambda_client.invoke(FunctionName=user_trf_arn, InvocationType='RequestResponse', Payload=json.dumps(data))
    response = {'statusCode':200}
    if response['statusCode'] == 200:
        # if the transfer was successful update 
        # each user available and in_loan
        # pool balance
        
        contribution_distribution = update_user_in_loan_and_pool_balance(pool_id, loan_amount)
        
        process_loan(username, loan_amount)
        
        # update to transaction history database
        transaction_details = {
            "transaction_type": "CREDIT",
            "amount": loan_amount,
            "pool_id": pool_id,
            "repaid": False,
            "contribution": contribution_distribution,
            "repayment_hist": {},
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

