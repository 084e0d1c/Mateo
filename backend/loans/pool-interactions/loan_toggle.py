import boto3
import simplejson as json
from dynamo_utils import update_loaning_toggle
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
    username = decode_username(event)
    loan_toggle_state = body['loan_toggle_state']
    
    update_loaning_toggle(username, loan_toggle_state)
    
    return {
        "statusCode": "200",
        "body": json.dumps({
            "message": "Successfully updated loaning toggle",
            "body": {"loaning_toggle": loan_toggle_state}
        }),
        "headers": {'Access-Control-Allow-Origin': "*"}
    }

