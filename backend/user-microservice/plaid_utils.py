import plaid
from plaid.api import plaid_api
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.country_code import CountryCode
from plaid.model.products import Products

from secrets_manager import get_plaid_key
import os

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
  request = LinkTokenCreateRequest(
    products=[Products('auth'), Products('transactions')],
    client_id=CLIENT_ID,
    client_name='Mateo',
    secret=get_plaid_key(),
    country_codes=[CountryCode('GB'), CountryCode('US')],
    language='en',
    user=LinkTokenCreateRequestUser(
      client_user_id=username
    )
  )
  # create link token
  response = client.link_token_create(request)
  return response['link_token']