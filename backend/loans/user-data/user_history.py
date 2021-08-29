import simplejson as json
import boto3
from boto3.dynamodb.conditions import Key
from os import environ
from utils import decode_username, exception_handler

dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
transaction_table = dynamodb.Table(environ.get('TRANSACTION_HISTORY_DATABASE_NAME'))

@exception_handler
def main(event, context):
    """
    Retrieve all of user historical transactions for loans with bank or pool

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
    
    transaction_details = transaction_table.query(
        IndexName="username",
        KeyConditionExpression=Key('username').eq(username))['Items']
    
    return {
        "statusCode": "200",
        "body": json.dumps({
            "message": "success",
            "body": transaction_details
        }),
        "headers": {'Access-Control-Allow-Origin': "*"}
    }

