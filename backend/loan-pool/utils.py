from functools import wraps, total_ordering
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

@total_ordering
class CreditRating(Enum):
    AA = 3
    BB = 2
    CC = 1
    
    def __lt__(self, other):
        # We can safely only consider the comparison between
        # CreditRating Enums.
        if self.__class__ is other.__class__:
            return self.value < other.value
    