import json
from os import environ
import boto3
from utils import exception_handler, decode_username
from internal_lambda_invoke_utils import invoke_check_balance_lambda, invoke_transfer_lambda, invoke_compute_credit_score_lambda



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

    repayment_amount = body['repayment_amount']
    uid = body['uid']
    
    username = decode_username(event)
    
    available_balance = invoke_check_balance_lambda({'username': username})
    
    if available_balance < repayment_amount:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Not enough funds available for repayment"}),
            "headers": {
                "Access-Control-Allow-Origin": "*"
            }
        }
    
    # invoke the transfer API 
    trf_data = {
        "amount": repayment_amount,
        "to": "MATEO",
        "username": username
    }
    
    response = invoke_transfer_lambda(trf_data)
    
    if response['statusCode'] == 200:
        # Recrunch credit score computation
        cred_data = {
            "username": username,
        }
        invoke_compute_credit_score_lambda(cred_data) # Fire and forget
        
        # Perform the repayment distribution to loaners
        
        
        # Log the successful transaction
        pool_hist_data = {
            "username": username,
            "amount": repayment_amount,
            "credit_debit": "debit",
            "pool_id": pool_id
        }
        pool_hist_arn = environ.get('POOL_HIST_LAMBDA')
        lambda_client.invoke(FunctionName=pool_hist_arn, InvocationType='Event', Payload=json.dumps(pool_hist_data))
        
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
        
        

