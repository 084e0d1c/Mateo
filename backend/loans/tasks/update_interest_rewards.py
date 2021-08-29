import boto3
import simplejson as json
from os import environ

dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
pool_table = dynamodb.Table(environ.get('POOL_DATABASE_NAME'))
loan_table = dynamodb.Table(environ.get('LOAN_DATABASE_NAME'))

def main(event, context):
    """
    Retrieve a list of a specific pool with business logic

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
    # Get Pool Interest Rates
    all_pools = pool_table.scan()['Items']
    interest_rates = {}
    for pool in all_pools:
        interest_rates[pool['pool_id']] = pool['interest_rate']
    
    # Update all user loan rewards
    all_users = loan_table.scan()['Items']
    # --------
    # TODO: Improve algorithm to O(n) or some vectorization if possible
    # --------
    for user in all_users:
        for pool_id in user['deposits_to_pools']:
            new_interests_yield = interest_rates[pool_id] * user['deposits_to_pools'][pool_id]['in_loan']
            user['deposits_to_pools'][pool_id]['interest_reward'] += new_interests_yield
            user['deposits_to_pools'][pool_id]['available'] += new_interests_yield
