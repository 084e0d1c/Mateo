import simplejson as json
from decimal import Decimal
from os import environ

import boto3

lambda_client = boto3.client('lambda', region_name='ap-southeast-1')

def invoke_transfer_lambda(payload):
    trf_lambda_name = environ.get('BANK_TRANSFER_LAMBDA')
    response = lambda_client.invoke(FunctionName=trf_lambda_name, InvocationType='RequestResponse', Payload=json.dumps(payload))
    response_payload = json.loads(response['Payload'].read().decode("utf-8"))
    print(response_payload)
    # -----------
    # HACK: Using status code to check if the transfer was successful
    # ------------
    if response_payload == "OK":
        return {'statusCode': 200}
    return {'statusCode': 400}

def invoke_check_balance_lambda(payload):
    bank_detail_lambda_name = environ.get('BANK_DETAIL_LAMBDA')
    user_detail_response = lambda_client.invoke(FunctionName=bank_detail_lambda_name, InvocationType='RequestResponse', Payload=json.dumps(payload))
    response_payload = json.loads(user_detail_response['Payload'].read().decode("utf-8"))
    user_detail_json = json.loads(response_payload['body'])['data']
    return Decimal(str(user_detail_json['plaid_account']['balances']['available']))

def invoke_compute_credit_metric_lambda(payload):
    cred_metric_lambda_name = environ.get('CREDIT_METRIC_LAMBDA')
    lambda_client.invoke(FunctionName=cred_metric_lambda_name, InvocationType='Event', Payload=json.dumps(payload))
