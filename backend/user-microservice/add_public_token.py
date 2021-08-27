import boto3
\
import os
import json
import jwt
from utils import exception_handler

from plaid_utils import get_access_token

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

  try:
    response = db_client.update_item(
      TableName=os.environ['USER_DATABASE_NAME'],
      Key={
        'username': {
          'S': username
        }
      },
      UpdateExpression='SET access_token = :access_token',
      ExpressionAttributeValues={
        ':access_token': {
          'S': get_access_token(public_token)
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

  return {
    "statusCode": "200",
    "body": json.dumps({
      "message": "success",
    }),
    "headers": {'Access-Control-Allow-Origin': "*"}
  }
