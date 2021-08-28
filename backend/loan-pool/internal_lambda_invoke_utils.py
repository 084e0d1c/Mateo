import json
from os import environ

import boto3

lambda_client = boto3.client('lambda', region_name='ap-southeast-1')

def invoke_transfer_lambda(payload):
    user_trf_arn = environ.get('USER_TRANSFER_LAMBDA')
    response = lambda_client.invoke(FunctionName=user_trf_arn, InvocationType='RequestResponse', Payload=json.dumps(payload))
    return response

def invoke_check_balance_lambda(payload):
    user_detail_arn = environ.get('USER_DETAIL_LAMBDA')
    user_detail_response = lambda_client.invoke(FunctionName=user_detail_arn, InvocationType='RequestResponse', Payload=json.dumps(payload))
    user_detail_json = json.loads(user_detail_response)
    return user_detail_json['available_balance']

def invoke_compute_credit_score_lambda(payload):
    compute_cred_arn = environ.get('COMPUTE_CRED_LAMBDA')
    lambda_client.invoke(FunctionName=compute_cred_arn, InvocationType='Event', Payload=json.dumps(payload))
    