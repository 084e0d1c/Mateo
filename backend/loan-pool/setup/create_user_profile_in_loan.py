import json
from decimal import Decimal
from os import environ

import boto3

dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
loan_table = dynamodb.Table(environ.get('LOAN_DATABASE_NAME'))
uid_table = dynamodb.Table(environ.get('USER_TRANSACTION_DATABASE_NAME'))

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
    username = event['username']
    
    user_detail = {
        "username": username,
        "max_loan_amount": Decimal("0"),
        "outstanding_loan_amount": Decimal("0"),
        "credit_rating": "CC",
        "deposits_to_pools": {},
        "loaning_toggle": False
    }
    
    loan_table.put_item(Item=user_detail)
    
    uid_detail = {
        "username": username,
        "uid": "" 
    }
    
    uid_table.put_item(Item=uid_detail)
    
    return {
        "statusCode": "200",
        "body": json.dumps({
            "message": "User profile in loan database created",
        }),
        "headers": {'Access-Control-Allow-Origin': "*"}
    }

