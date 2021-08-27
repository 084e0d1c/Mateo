import boto3

import os
import json
from utils import exception_handler

cognito_client = boto3.client('cognito-idp', region_name='ap-southeast-1')

@exception_handler
def main(event, context):
    """
    Logs in user in Cognito

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

    password = body["password"]
    username = body["username"]

    # Logs in user for Cognito
    response = cognito_client.initiate_auth(
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            'USERNAME': username,
            'PASSWORD': password
        },
        ClientId=os.environ['COGNITO_CLIENT_ID'],
    )

    # Returns the accessToken for authorized requests
    return {
        "statusCode": "200",
        "body": json.dumps(response['AuthenticationResult']),
        "headers": {'Access-Control-Allow-Origin': "*"}
    }
