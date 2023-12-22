import jwt
from django.conf import settings
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework import status
from utils import date_time_utils


class JWTAuthMiddleware(MiddlewareMixin):
    """
        For checking if auth token is valid or not. In case of failure exception will be raised.
    """

    def process_request(self, request):
        auth_check = self.user_auth(request)
        if auth_check is not True:
            return auth_check


    @staticmethod
    def user_auth(request):

        exclusion_list = {'/api/v1/user/signup/',
                          '/api/v1/user/login/',
                          '/api/v1/user/refresh-token/',
                          '/api/v1/company/dropdown-list/',
                          '/api/v1/company/create/'}
       
        if request.path in exclusion_list:
            return True
        
        error_payload = {"status": status.HTTP_401_UNAUTHORIZED, "message": "Invalid Token."}
        jwt_token = request.headers.get("authorization")

        try:
            payload = jwt.decode(jwt_token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
        
            current_datetime = date_time_utils.get_current_datetime()
            current_datetime = int(current_datetime.timestamp())
            expiry = payload['exp']
       
            if current_datetime > expiry:
                return JsonResponse(error_payload, status=status.HTTP_401_UNAUTHORIZED)
            setattr(request, 'user_details', payload['user_details'])

        except (jwt.ExpiredSignatureError, jwt.DecodeError, jwt.InvalidTokenError) as e:
            return JsonResponse(error_payload, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return JsonResponse(error_payload, status=status.HTTP_401_UNAUTHORIZED)

        return True
