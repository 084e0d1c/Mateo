import plaid
from plaid.api import plaid_api
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.accounts_get_request import AccountsGetRequest

from plaid.model.country_code import CountryCode
from plaid.model.products import Products

from secrets_manager import get_plaid_key
import os
import ast

CLIENT_ID = "6127c5c51489d0000e28c6aa"

# Available environments are 'Production' | 'Development' | 'Sandbox'
# Client ID is safe to publish
configuration = plaid.Configuration(
  host=plaid.Environment.Production if os.environ["PYTHON_ENV"] == 'prod' else plaid.Environment.Sandbox,
  api_key={
    'clientId': CLIENT_ID,
    'secret': get_plaid_key(),
  }
)

api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)

def get_access_token(public_token: str) -> str:
  exchange_request = ItemPublicTokenExchangeRequest(
    public_token=public_token
  )
  exchange_response = client.item_public_token_exchange(exchange_request)
  return exchange_response['access_token']

def get_plaid_link_token(username: str) -> str:
  """Retrieves plaid link token to initiate plaid UI in frontend

  Args:
      username (str)

  Returns:
      str: link_token
  """
  request = LinkTokenCreateRequest(
    products=[Products('auth'), Products('transactions')],
    client_name='Mateo',
    country_codes=[CountryCode('GB'), CountryCode('US')],
    language='en',
    user=LinkTokenCreateRequestUser(
      client_user_id=username
    )
  )
  # create link token
  response = client.link_token_create(request)
  return response['link_token']

def get_plaid_first_account(access_token: str) -> str:
  """Retrieves first linked bank account from plaid

  Args:
      access_token (str)

  Returns:
      dict: https://plaid.com/docs/api/accounts/
  """
  request = AccountsGetRequest(access_token=access_token)
  response = client.accounts_get(request)
  return ast.literal_eval(response['accounts'][0].__str__())