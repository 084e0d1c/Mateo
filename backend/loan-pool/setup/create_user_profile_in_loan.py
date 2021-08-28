import json
from os import environ
from decimal import Decimal
import boto3
from utils import exception_handler

dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
loan_table = dynamodb.Table(environ.get('LOAN_DATABASE_NAME'))
uid_table = dynamodb.Table(environ.get('USER_TRANSACTION_DATABASE_NAME'))

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
    # body = json.loads(event) # internal invoke no API Gateway body
    
    # ---------------
    # TODO: Integrate with User signup to create account
    # ---------------
    # username = body['username']
    username = "BBB"
    
    user_detail = {
        "username": username,
        "max_loan_amount": Decimal("0"),
        "outstanding_loan_amount": Decimal("0"),
        "credit_rating": "C",
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

