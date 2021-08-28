import simplejson as json

import boto3
from dynamo_utils import check_pool_eligibility
from utils import decode_username, exception_handler


@exception_handler
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
    
    body = json.loads(event['body'])
    pool_id = body['pool_id']
    username = decode_username(event)
    
    # Business Logic: Check and add params to indicate eligiblity for loan / deposit
    pool_detail = check_pool_eligibility(username, pool_id)
    
    return {
        "statusCode": "200",
        "body": json.dumps({
            "message": "success",
            "body": pool_detail
        }),
        "headers": {'Access-Control-Allow-Origin': "*"}
    }

