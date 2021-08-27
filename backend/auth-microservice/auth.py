import boto3

import os
import json
from functools import wraps
from json import JSONDecodeError

# Returns errors in response for easier debugging
def exception_handler(handler):
    @wraps(handler)
    def handler_with_exception(*args, **kwargs):
        try:
            return handler(*args, **kwargs)
        except Exception as err:
            return {
                "statusCode": "400",
                "body": "Error: " + str(err),
                "headers": {'Access-Control-Allow-Origin': "*"}
            }

    return handler_with_exception


client = boto3.client('cognito-idp', region_name='ap-southeast-1')

@exception_handler
def signup(event, context):
    """
    Signs up user in Cognito

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

    email = body["email"]
    password = body["password"]
    username = body["username"]

    # Signs up in Cognito
    response = client.sign_up(
        ClientId=os.environ['COGNITO_CLIENT_ID'],
        Username=username,
        Password=password,
        UserAttributes=[
            {
                'Name': 'email',
                'Value': email
            },
        ],
    )

    # Verifies the email automatically
    # If not user cannot log in
    # This is for prototyping purpose
    response = client.admin_confirm_sign_up(
        UserPoolId=os.environ['COGNITO_USERPOOL_ID'],
        Username=username
    )

    # TODO: Save additional attributes to DynamoDB if necessary


    return {
        "statusCode": "200",
        "body": json.dumps({
            "message": "success"
        }),
        "headers": {'Access-Control-Allow-Origin': "*"}
    }
