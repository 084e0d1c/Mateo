import json
from decimal import Decimal
from os import environ

import boto3
from utils import CreditRating

dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
loan_table = dynamodb.Table(environ.get('LOAN_DATABASE_NAME'))

def main(event, context):
    """
    Lambda to compute credit scores based on an arbitrary criteria.

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
    
    username = event['username']
    user_detail = loan_table.get_item(Key={"username": username})['Item']
    
    # Business Logic: Credit Rating Score * balance floor 2 (this is arbitrary)
    max_loan_amount = (CreditRating[user_detail['credit_rating']] * user_detail['bank_balance']) // 2
    user_detail['max_loan_amount'] = Decimal(str(max_loan_amount))
    
    # ----------
    # TODO: Design a way to upgrade or downgrade credit ratings
    # Ideas:
    # 1 - Check how much balance the user has in the account for past 30 days
    # 2 - If user is constantly leveraged, then high risk profile
    # 3 - Speed of repayment is a good indicator of credit risk
    # ----------
    # )
    loan_table.put_item(Item=user_detail)
    
    return {
        "statusCode": "200",
        "body": json.dumps({
            "message": "Credit Metrics successfully updated",
        }),
        "headers": {'Access-Control-Allow-Origin': "*"}
    }

