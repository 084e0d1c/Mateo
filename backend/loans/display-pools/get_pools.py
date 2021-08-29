from os import environ
from decimal import Decimal
import boto3
import simplejson as json
from dynamo_utils import scan_all_pools, update_bank_balance
from utils import decode_username, exception_handler
from internal_lambda_invoke_utils import invoke_check_balance_lambda

@exception_handler
def main(event, context):
    """
    Lambda to retrieve all pools from DynamoDB and return them as a JSON string.

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
    # Scan the table and return all pools (which there are only 3-4)
    # Additionally check credit ratings etc to see if eligible
    username = decode_username(event)
    pool_details = scan_all_pools(username)
    
    # --------
    # HACK: Update the user bank balance whenever they check the page
    # --------
    bank_balance = invoke_check_balance_lambda(event)
    username = decode_username(event)
    update_bank_balance(username, bank_balance)
    
    # Update max deposit into pool_details as 50% of their bank balance
    # We put a generic amount into each pool, which can be adjusted later on
    for pool in pool_details:
        pool['max_deposit'] = Decimal(str(0.5)) * bank_balance
    
    return {
        "statusCode": "200",
        "body": json.dumps({
            "message": "success",
            "body": pool_details
        }),
        "headers": {'Access-Control-Allow-Origin': "*"}
    }

