import boto3

import os

db_client = boto3.client('dynamodb')

def main(params):
  """Initiate bank transfer and notify via SMS

  Args:
      params (dict): {
          amount: <int>,
          to: "MATEO" | "USER",
          username: <str>
        }
  """
  try:

    assert 'amount' in params and params['amount'].isnumeric()
    assert 'to' in params and params['to'] in ['MATEO', 'USER']
    assert 'username' in params

    amount = params['amount']
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

    if 'to' == "MATEO":
      pass

    elif 'to' == "USER":
      pass

  except Exception as err:
    print(err)
    return "ERROR"

  return "OK"
