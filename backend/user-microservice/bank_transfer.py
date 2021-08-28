import boto3

import os
import json

from plaid_utils import execute_bank_transfer
from secrets_manager import get_mateo_plaid_account_id, get_mateo_plaid_token

db_client = boto3.client('dynamodb')
sns_client = boto3.client('sns')

# 
# Invoke to test the function in deployment environment
#
# sls invoke --function BankTransfer --stage dev --region ap-southeast-1 --aws-profile brandon --data '{ "amount": 10, "to": "MATEO", "username": "phyo" }'
#

def main(params, context):
  """Initiate bank transfer and notify via SMS

  Args:
      params (dict): {
          amount: <int>,
          to: "MATEO" | "USER",
          username: <str>
        }
  """
  try:
    assert 'amount' in params and (isinstance(params['amount'], int) or isinstance(params['amount'], float))
    assert 'to' in params and params['to'] in ['MATEO', 'USER']
    assert 'username' in params

    amount = float(params['amount'])
    to = params['to']
    username = params['username']
  
    # Get user item from database
    response = db_client.get_item(
      TableName=os.environ['USER_DATABASE_NAME'],
      Key={
        'username': {
          'S': username
        }
      }
    )

    user_details_dict = { 
      key: value["S"] for key, value in response['Item'].items()
    }

    if 'access_token' not in user_details_dict:
      return "UNLINKED"

    if to == "MATEO":
      execute_bank_transfer(
        user_details_dict['access_token'],
        get_mateo_plaid_account_id(),
        user_details_dict['fullname'],
        amount
      )
      try:
        sns_client.publish(
          PhoneNumber=user_details_dict['phone'],
          Message=f"Transfer to Mateo: ${amount} is processing",
          Subject="Mateo Bank Transfer"
        )
      except err:
        # For demo, we have not added phone verification
        # So bad numbers may raise error
        print(err)
        pass

    elif to == "USER":
      execute_bank_transfer(
        get_mateo_plaid_token(),
        user_details_dict['account_id'],
        "Mateo Admin",
        amount
      )
      try:
        sns_client.publish(
          PhoneNumber=user_details_dict['phone'],
          Message=f"Transfer from Mateo: ${amount} is processing",
          Subject="Mateo Bank Transfer"
        )
      except err:
        print(err)
        pass

  except Exception as err:
    print(err)
    return "ERROR"

  return "OK"
