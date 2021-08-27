import boto3

import os
import json
from utils import exception_handler

client = boto3.client('cognito-idp', region_name='ap-southeast-1')

@exception_handler
def main(event, context):
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
