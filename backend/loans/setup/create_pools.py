import json
from decimal import Decimal
from os import environ

import boto3

dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
pool_table = dynamodb.Table(environ.get('POOL_DATABASE_NAME'))

def main(event, context):
    """
    Lambda to initiailse the loan pools

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
    REPAYMENT_SCHEDULE = "3 months"
    ADMIN_FEE = Decimal("0.0001")
    pools_to_create = [{
               "pool_id": "Gold",
                "available_amount": 0,
                "interest_rate": Decimal("0.01"),
                "credit_rating_requirement": "BB",
                "contribution_distribution": {},
                "administrative_fees": ADMIN_FEE, # 0.01% 
                "repayment_schedule": REPAYMENT_SCHEDULE,
                "risk_level": "Low"
           }, {
               "pool_id": "Sliver",
                "available_amount": 0,
                "interest_rate": Decimal("0.03"),
                "credit_rating_requirement": "CC",
                "contribution_distribution": {},
                "administrative_fees": ADMIN_FEE, # 0.01% 
                "repayment_schedule": REPAYMENT_SCHEDULE,
                "risk_level": "Medium"
           }, {
               "pool_id": "Bronze",
               "available_amount": 0,
               "interest_rate": Decimal("0.05"),
               "credit_rating_requirement": "DD",
               "contribution_distribution": {},
               "administrative_fees": ADMIN_FEE, # 0.01% 
                "repayment_schedule": REPAYMENT_SCHEDULE,
                "risk_level": "High"
           }   
    ]
    
    for pool in pools_to_create:
        pool_table.put_item(Item=pool)
        
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Pools init success",
        }),
        "headers": {'Access-Control-Allow-Origin': "*"}
    }

