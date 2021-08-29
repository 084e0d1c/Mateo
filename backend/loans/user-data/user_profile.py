from os import environ

import boto3
import simplejson as json
from dynamo_utils import check_pool_eligibility
from utils import decode_username, exception_handler

dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
loan_table = dynamodb.Table(environ.get('LOAN_DATABASE_NAME'))

@exception_handler
def main(event, context):
    """
    Retrieve a list of a specific pool with business logic

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
    
    username = decode_username(event)
    
    user_profile = loan_table.get_item(Key={'username': username})['Item']
    
    return {
        "statusCode": "200",
        "body": json.dumps({
            "message": "success",
            "body": user_profile
        }),
        "headers": {'Access-Control-Allow-Origin': "*"}
    }

