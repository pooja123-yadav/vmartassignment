from rest_framework.views import APIView
from utils.responses import prepare_response, RESPONSES
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import check_password, make_password
from apps.users.controllers import user_controller



class CreateUserAPI(APIView):
    def post(self, request):
        body = request.data
        
        email = body.get("email")
        password = body.get("password")
        company = body.get("comapny")

        if not company:
           raise ValidationError("Please select company") 

        if not email:
            raise ValidationError("Email cannot be empty")

        if not password:
            raise ValidationError("Password cannot be empty")
        
        confirm_password = body.get("confirm_password")
        if password != confirm_password:
            raise ValidationError("Password and confirm password are not same")

        user_controller.create_user(**body)

        return prepare_response(RESPONSES.GENERIC.SUCCESS, data=[])


class UpdateUserAPI(APIView):
    def post(self, request):
       
        body = request.data

        user_id = body.get('id')
        if not user_id:
            raise ValidationError("User not found")
        
        auth_user_id = request.user_details.get('user_id')
        if auth_user_id != user_id:
            raise ValidationError("You are not authorized to update details")
        
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
            raise ValidationError("Email cannot be empty")

        if not password:
            raise ValidationError("Password cannot be empty")
        
        response_data = user_controller.login_user(**body)

        return prepare_response(RESPONSES.GENERIC.SUCCESS, data=response_data)


class RefreshTokenAPI(APIView):

    def post(self, request):
        refresh_token = request.data.get("refresh_token")

        response = user_controller.refresh_access_token(refresh_token=refresh_token)

        return prepare_response(RESPONSES.GENERIC.SUCCESS, data=response)


class LogoutUserAPI(APIView):
    def get(self, request):
        body = request.data
        auth_user = request.user_details

        refresh_token = body.get('refresh_token')
        if not refresh_token:
            raise ValidationError('Invalid Refresh Token')
        
        user_controller.logout_user(**body)
