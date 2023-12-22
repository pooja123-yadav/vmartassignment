from rest_framework.views import APIView
from utils.responses import prepare_response, RESPONSES, raise_error
from rest_framework.exceptions import ValidationError
from apps.users.controllers import user_controller


class CreateUserAPI(APIView):
    def post(self, request):
        body = request.data
        
        email = body.get("email")
        password = body.get("password")
        company = body.get("company_id")

        if not company:
           raise_error(RESPONSES.USER.ERRORS.COMPANY_MISSING)

        if not email:
            raise_error(RESPONSES.USER.ERRORS.USER_EMAIL_MISSING)

        if not password:
            raise_error(RESPONSES.USER.ERRORS.USER_PASSWORD_MISSING)
        
        confirm_password = body.get("confirm_password")
        if password != confirm_password:
            raise_error(RESPONSES.USER.ERRORS.CONFIRM_PASSWORD_MISMATCH)

        user_controller.create_user(**body)

        return prepare_response(RESPONSES.GENERIC.SUCCESS, data=[])


class UpdateUserAPI(APIView):
    def post(self, request):
       
        body = request.data

        user_id = body.get('id')
        if not user_id:
            raise_error(RESPONSES.ERRORS.VALIDATIONS.USER_ID_MISSING)
        
        auth_user_id = request.user_details.get('user_id')
        if auth_user_id != user_id:
            raise_error(RESPONSES.ERRORS.VALIDATIONS.NOT_UNAUTHORIZED)
        
        response_data = user_controller.update_user(**body)

        return prepare_response(RESPONSES.GENERIC.SUCCESS, data=response_data)


class GetUserDetailAPI(APIView):
    def get(self, request):
        auth_user = request.user_details
        
        response_data = user_controller.get_user_detail(**auth_user)

        return prepare_response(RESPONSES.GENERIC.SUCCESS, data=response_data)


class LoginUserAPI(APIView):
    def post(self, request):
        body = request.data

        email = body.get("email")
        password = body.get("password")

        if not email:
            raise_error(RESPONSES.USER.ERRORS.USER_EMAIL_MISSING)

        if not password:
            raise_error(RESPONSES.USER.ERRORS.USER_PASSWORD_MISSING)
        
        response_data = user_controller.login_user(**body)

        return prepare_response(RESPONSES.GENERIC.SUCCESS, data=response_data)


class RefreshTokenAPI(APIView):

    def post(self, request):
        refresh_token = request.data.get("refresh_token")

        if not refresh_token:
            raise_error(RESPONSES.ERRORS.VALIDATIONS.REFRESH_TOKEN_MISSING)

        response = user_controller.refresh_access_token(refresh_token=refresh_token)

        return prepare_response(RESPONSES.GENERIC.SUCCESS, data=response)


class LogoutUserAPI(APIView):
    def post(self, request):
        body = request.data
        auth_user = request.user_details

        refresh_token = body.get('refresh_token')
        if not refresh_token:
            raise_error(RESPONSES.ERRORS.VALIDATIONS.REFRESH_TOKEN_MISSING)
        
        user_controller.logout_user(**body)

        return prepare_response(RESPONSES.GENERIC.SUCCESS, data=[])
