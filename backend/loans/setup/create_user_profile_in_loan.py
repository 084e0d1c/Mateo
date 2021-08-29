import json
from decimal import Decimal
from os import environ
from internal_lambda_invoke_utils import invoke_compute_credit_metric_lambda
import boto3

dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')
loan_table = dynamodb.Table(environ.get('LOAN_DATABASE_NAME'))
uid_table = dynamodb.Table(environ.get('USER_TRANSACTION_DATABASE_NAME'))

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
    username = event['username']
    # Business Logic: Assume everyone starts at BB rating
    # Max Loan will be computed later
    # ------------
    # HACK: For this hackathon, we assume some bank loans that are already in place, 
    # As we are unable to interface with plaid for loans in sandbox
    # ------------
    user_detail = {
        "username": username,
        "max_loan_amount": Decimal("0"),
        "outstanding_loan_amount": Decimal("0"), # This should change to outstanding_pool_loan
        "credit_rating": "BB",
        "deposits_to_pools": {},
        "loans_from_pools": {},
        "loans_from_banks": {
            "Personal Loan": {
                "interest_rate": Decimal("0.047"),
                "next_payment_due_days": "13",
                "payment_period_months": "2",
                "amount_repaid": Decimal("600"),
                "amount_remaining": Decimal("300")
            },
            "Home Loan": {
                "interest_rate": Decimal("0.039"),
                "next_payment_due_days": "17",
                "payment_period_months": "12",
                "amount_repaid": Decimal("833"),
                "amount_remaining": Decimal("150")
            },
            "Credit Card Loan": {
                "interest_rate": Decimal("0.064"),
                "next_payment_due_days": "21",
                "payment_period_months": "24",
                "amount_repaid": Decimal("405"),
                "amount_remaining": Decimal("270")
            }
        },
        "loaning_toggle": False
    }
    
    loan_table.put_item(Item=user_detail)
    
    uid_detail = {
        "username": username,
        "uid": "" 
    }
    
    uid_table.put_item(Item=uid_detail)
    
    invoke_compute_credit_metric_lambda(event)
    
    return {
        "statusCode": "200",
        "body": json.dumps({
            "message": "User profile in loan database created",
        }),
        "headers": {'Access-Control-Allow-Origin': "*"}
    }

