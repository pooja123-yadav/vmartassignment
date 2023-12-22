from rest_framework.response import Response
from middlewares.exceptions import CustomError

class RESPONSES:
    class GENERIC:
        SUCCESS = (101, "Success", 200)
        FAILURE = (102, "Oops, Something went wrong!", 500)
        UNAUTHORIZED = (103, "Unauthorized", 401)

    class INVALID:
        NETWORK_CALL = (201, "Invalid Request in network call", 500)

    class ERRORS:
        class VALIDATIONS:
            REFRESH_TOKEN_MISSING = (401, "Refresh token is missing", 400)
            INVALID_REFRESH_TOKEN = (402, "Invalid refresh token", 400)
            USER_ID_MISSING = (403, "User ID is missing", 400)
            NOT_UNAUTHORIZED = (404, "You are not authorized to update details", 400)
            ADD_USER_VALIDATION_FAILED = (405, "Add user validation error", 400)
    
    class USER:
        class ERRORS:
            DOES_NOT_EXIST = (601, "User does not exist", 400)
            COMPANY_MISSING = (602, "Please select company", 400)
            COMPANY_DOES_NOT_EXIST = (603, "Selected company is not exist", 400)
            USER_EMAIL_MISSING = (604,"Please enter user email", 400)
            USER_PASSWORD_MISSING = (605,"Please enter user password", 400)
            INVALID_USER_EMAIL = (606,"Invalid password", 400)
            INVALID_USER_PASSWORD = (607,"Invalid password", 400)
            CONFIRM_PASSWORD_MISMATCH = (608, "Password and confirm password are not same", 400)

def prepare_response(response=RESPONSES.GENERIC.SUCCESS, data=None, extras=None):
    response_payload = {
        "status": response[0],
        "message": response[1],
        "data": data
    }
    if extras:
        response_payload.update(extras)
    return Response(response_payload, status=response[2])


def raise_error(error=None, message=None, status=None):
    if not error:
        error = (0, message, status)
    error = list(error)
    if message:
        error[1] = message
    if status:
        error[2] = status
    raise CustomError({
        "status": error[0],
        "message": error[1],
    }, error[2])