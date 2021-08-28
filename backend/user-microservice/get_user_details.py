import boto3

import os
import json
import jwt
from utils import exception_handler

from plaid_utils import get_plaid_first_account

db_client = boto3.client('dynamodb')

@exception_handler
def main(event, context):
  """
  Gets user details

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

  try:
    response = db_client.get_item(
      TableName=os.environ['USER_DATABASE_NAME'],
      Key={
        'username': {
          'S': username
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

  user_details_dict = { key: value["S"] for key, value in response['Item'].items() if key != 'access_token' }

  ## Get plaid linked bank account details
  if 'access_token' in response['Item']:
    user_details_dict['plaid_account'] = get_plaid_first_account(response['Item']['access_token']["S"])
  else:
    user_details_dict['plaid_account'] = None

  return {
    "statusCode": "200",
    "body": json.dumps({
      "message": "success",
      "data": user_details_dict
    }),
    "headers": {'Access-Control-Allow-Origin': "*"}
  }