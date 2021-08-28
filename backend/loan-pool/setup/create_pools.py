import json
from os import environ

import boto3
from utils import exception_handler, decode_username
from dynamo_utils import scan_all_pools

dynamo_client = boto3.client('dynamodb', region_name='ap-southeast-1')
pool_table = dynamo_client.Table(environ.get('POOL_DATABASE_NAME'))

@exception_handler
def main(event, context):
    """
    Lambda to retrieve all pools, with business logic to segment eligible and ineligible pools

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
    pools_to_create = {
           "Gold": {
                "available_amount": 0,
                "interest_rate": 0.01,
                "credit_rating_requirement": "AA",
                "contribution_distribution": {}   
           },
           "Sliver": {
                "available_amount": 0,
                "interest_rate": 0.03,
                "credit_rating_requirement": "BB",
                "contribution_distribution": {}
           },
           "Bronze": {
               "available_amount": 0,
               "interest_rate": 0.05,
               "credit_rating_requirement": "CC",
               "contribution_distribution": {}
           }   
    }
    
    for pool in pools_to_create:
        pool_item = {
            "pool_id": pool,
            "pool_details": pools_to_create[pool]
        }
        pool_table.put_item(Item=pool_item)
    return {
        "statusCode": "200",
        "body": json.dumps({
            "message": "Pools init success",
        }),
        "headers": {'Access-Control-Allow-Origin': "*"}
    }

