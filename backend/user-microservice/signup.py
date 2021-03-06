import boto3

import os
import json
from utils import exception_handler
from plaid_utils import get_access_token

lambda_client = boto3.client('lambda', region_name='ap-southeast-1')
cognito_client = boto3.client('cognito-idp', region_name='ap-southeast-1')
db_client = boto3.client('dynamodb')

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
    phone = body["phone"]
    fullname = body["fullname"]

    # Signs up in Cognito
    try:
        response = cognito_client.sign_up(
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
    except Exception as err:
        if 'UsernameExistsException' in str(err):
            err = 'username already exists'
        return {
            "statusCode": "400",
            "body": json.dumps({
                "message": str(err)
            }),
            "headers": {'Access-Control-Allow-Origin': "*"}
        }

    # Verifies the email automatically. If not user cannot log in
    response = cognito_client.admin_confirm_sign_up(
        UserPoolId=os.environ['COGNITO_USERPOOL_ID'],
        Username=username
    )

    #
    # TODO: Save additional attributes to DynamoDB if necessary
    #
    try:
        response = db_client.put_item(
            TableName=os.environ['USER_DATABASE_NAME'],
            Item={
                'email': {
                    'S': email
                },
                'username': {
                    'S': username
                },
                'phone': {
                    'S': phone
                },
                'fullname': {
                    'S': fullname
                }
            }
        )   
    except Exception as err:
        return {
            "statusCode": "400",
            "body": json.dumps({
                "message": str(err)
            }),
            "headers": {'Access-Control-Allow-Origin': "*"}
        }

    # # Invoke create user loan profile fire-forget
    create_user_loan_profile_arn = os.environ.get('COMPUTE_USER_LOAN_PROFILE_LAMBDA')
    lambda_client.invoke(FunctionName=create_user_loan_profile_arn, InvocationType='Event', Payload=json.dumps({ "username": username }))
    
    return {
        "statusCode": "200",
        "body": json.dumps({
            "message": "success"
        }),
        "headers": {'Access-Control-Allow-Origin': "*"}
    }
