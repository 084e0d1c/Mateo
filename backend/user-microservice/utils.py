from functools import wraps

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