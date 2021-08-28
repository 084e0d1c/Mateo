import json
from os import environ

import boto3
from utils import exception_handler

dynamo_client = boto3.client('dynamodb', region_name='ap-southeast-1')
loan_table = dynamo_client.Table(environ.get('LOAN_DATABASE_NAME'))

@exception_handler
def main(event, context):
    """
    Lambda to retrieve all pools, with business logic to segment eligible and ineligible pools

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
    username = body['username']
    
    user_detail = {
        "username": username,
        "user_details": {
            "max_loan_amount": 0,
            "outstanding_loan_amount": 0,
            "credit_rating": "C",
            "deposits_to_pools": {},
            "loaning_toggle": False
        }    
    }
    
    loan_table.put_item(Item=user_detail)
    
    return {
        "statusCode": "200",
        "body": json.dumps({
            "message": "User profile in loan database created",
        }),
        "headers": {'Access-Control-Allow-Origin': "*"}
    }

