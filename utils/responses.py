from rest_framework.response import Response

class RESPONSES:
    class GENERIC:
        SUCCESS = (101, "Success", 200)
        FAILURE = (102, "Oops, Something went wrong!", 500)
        UNAUTHORIZED = (103, "Unauthorized", 401)

    class INVALID:
        NETWORK_CALL = (201, "Invalid Request in network call", 500)

    class ERRORS:
        class VALIDATIONS:
            pass

def prepare_response(response=RESPONSES.GENERIC.SUCCESS, data=None, extras=None):
    response_payload = {
        "status": response[0],
        "message": response[1],
        "data": data
    }
    if extras:
        response_payload.update(extras)
    return Response(response_payload, status=response[2])


