import boto3
import os
import json

from botocore.exceptions import ClientError

def get_plaid_key():
  """Retrieves plaid API key from secrets manager

  Returns:
      [string]: Plaid secret API key
  """
  plaid_key_secret_id = os.environ["PYTHON_ENV"] + "/plaid/key"

  # Create a Secrets Manager client
  session = boto3.session.Session()
  client = session.client(service_name='secretsmanager')

  try:
    plaid_key_secret_response = client.get_secret_value(SecretId=plaid_key_secret_id)
  except ClientError as e:
    print(e)
  else:
    plaid_key_secret = json.loads(plaid_key_secret_response['SecretString'])[plaid_key_secret_id]

  return plaid_key_secret