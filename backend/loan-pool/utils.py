from functools import wraps
from enum import Enum
import jwt

# Returns errors in response for easier debugging
def exception_handler(handler):
    @wraps(handler)
    def handler_with_exception(*args, **kwargs):
        try:
            return handler(*args, **kwargs)
        except Exception as err:
            return {
                "statusCode": "500",
                "body": "Internal Error: " + str(err),
                "headers": {'Access-Control-Allow-Origin': "*"}
            }

    return handler_with_exception

def decode_username(event):
    """Decode username from the JWT token

    Args:
        event (dict): Lambda event.

    Returns:
        (str): username
    """
    cognito_access_token = event['headers']["Authorization"].split(" ")[1]
    username = jwt.decode(cognito_access_token, options={"verify_signature": False})["username"]
    return username

class CreditDebit(Enum):
    CREDIT = -1
    DEBIT = 1
    
    def __mul__(self, other):
        return self.value * other
    
class CreditRating(Enum):
    AA = 3
    BB = 2
    CC = 1
    
    def __lt__(self, other):
        return self.value < other.value
    