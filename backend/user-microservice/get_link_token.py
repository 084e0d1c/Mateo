import os
import json
import jwt
from utils import exception_handler

from plaid_utils import get_plaid_link_token

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

  return {
    "statusCode": "200",
    "body": json.dumps({
      "message": "success",
      "data": {
        "link_token": get_plaid_link_token(username)
      }
    }),
    "headers": {'Access-Control-Allow-Origin': "*"}
  }
