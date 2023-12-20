from rest_framework.views import APIView
from utils.responses import prepare_response, RESPONSES
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import check_password, make_password
from apps.users.controllers import user_controller

class LoginUser(APIView):
    def post(self, request):
        body = request.data

        email = body.get("email")
        password = body.get("password")

        if not email:
            raise ValidationError("Email cannot be empty")

        if not password:
            raise ValidationError("Password cannot be empty")
        
        user_controller.login_user(**body)

class LogoutUser(APIView):
    def post(self, request):
        pass

class CreateUser(APIView):
    def post(self, request):
        body = request.data
        user_controller.create_user(**body)

class UpdateUser(APIView):
    def post(self, request):
        body = request.data
        user_id = body.get('user_id')

        if not user_id:
            raise ValidationError("User not found")

        user_controller.update_user(**body)

class GetUserDetailById(APIView):
    def post(self, request):
        pass

