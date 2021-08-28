from os import environ

import boto3
import simplejson as json
from dynamo_utils import scan_all_pools
from utils import decode_username, exception_handler


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
    response = scan_all_pools()
    
    return {
        "statusCode": "200",
        "body": json.dumps({
            "message": "success",
            "body": response
        }),
        "headers": {'Access-Control-Allow-Origin': "*"}
    }

