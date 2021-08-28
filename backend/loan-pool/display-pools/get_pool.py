import json
import boto3
from utils import exception_handler, decode_username
from dynamo_utils import check_pool_eligibility

@exception_handler
def main(event, context):
    """
    User remove their original contribution from the pool.

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
    
    # Check for user credit rating
    pool_detail = check_pool_eligibility(username, pool_id)
    
    return {
        "statusCode": "200",
        "body": json.dumps({
            "message": "success",
            "body": pool_detail
        }),
        "headers": {'Access-Control-Allow-Origin': "*"}
    }

