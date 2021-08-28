import boto3
import os
import json

from botocore.exceptions import ClientError

def get_mateo_plaid_token() -> str:
  """Retrieves Mateo plaid access token from secrets manager

  Returns:
      [string]: Plaid access token
  """
  mateo_plaid_token_secret_id = os.environ["PYTHON_ENV"] + "/mateo/plaid/token"
  return get_secret_by_key(mateo_plaid_token_secret_id)

def get_plaid_key() -> str:
  """Retrieves plaid API key from secrets manager

  Returns:
      [string]: Plaid secret API key
  """
  plaid_key_secret_id = os.environ["PYTHON_ENV"] + "/plaid/key"
  return get_secret_by_key(plaid_key_secret_id)

def get_secret_by_key(secret_id: str) -> str:
  """Retrieves secret from secrets manager

  Returns:
      [string]: Secret value
  """
  # Create a Secrets Manager client
  session = boto3.session.Session()
  client = session.client(service_name='secretsmanager')

  try:
    secret_response = client.get_secret_value(SecretId=secret_id)
  except ClientError as e:
    print(e)
  else:
    secret_value = json.loads(secret_response['SecretString'])[secret_id]

  return secret_value