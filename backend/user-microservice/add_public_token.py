import boto3
\
import os
import json
import jwt
from utils import exception_handler

from plaid_utils import get_access_token, get_plaid_first_account

db_client = boto3.client('dynamodb')

@exception_handler
def main(event, context):
  """
  Retrieves plaid token

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
  cognito_access_token = event['headers']["Authorization"].split(" ")[1]
  username = jwt.decode(cognito_access_token, options={"verify_signature": False})["username"]

  body = json.loads(event['body'])
  public_token = body["public_token"]

  # Get access token from plaid
  plaid_access_token = get_access_token(public_token)
  # Get first account ID from plaid
  account_id = get_plaid_first_account(plaid_access_token)['account_id']

  try:
    response = db_client.update_item(
      TableName=os.environ['USER_DATABASE_NAME'],
      Key={
        'username': {
          'S': username
        }
      },
      UpdateExpression='SET access_token = :access_token, account_id: :account_id',
      ExpressionAttributeValues={
        ':access_token': {
          'S': plaid_access_token
        },
        ':account_id': {
          'S': account_id
        },
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

  return {
    "statusCode": "200",
    "body": json.dumps({
      "message": "success",
    }),
    "headers": {'Access-Control-Allow-Origin': "*"}
  }
