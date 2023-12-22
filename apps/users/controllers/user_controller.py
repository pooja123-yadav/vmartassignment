from django.contrib.auth.hashers import check_password, make_password
from apps.users.db_controllers import user_db
from apps.companies.db_controllers import company_db
from rest_framework.exceptions import ValidationError
from apps.users.serializer import UserSerializer
from apps.users import utils as user_utils
from django.db import transaction
from utils import date_time_utils
from utils.responses import RESPONSES, raise_error
    

# Create a User
def create_user(**kwargs):
   
    raw_password = kwargs.get('password')

    del kwargs['password']
    del kwargs['confirm_password']

    company_filter = {"id":kwargs.get('company_id')}

    get_company  = company_db.get_company_detail(**company_filter)
    if not get_company:
        raise_error(RESPONSES.USER.ERRORS.COMPANY_DOES_NOT_EXIST)

    user_serializer = UserSerializer(data=kwargs)

    if user_serializer.is_valid():
        with transaction.atomic():
            user_serializer.save()
            user_password = {
                "user_id": user_serializer.data['id'],
                "password_hash": make_password(raw_password)  # using the raw_password here
            }
            user_db.save_user_password(**user_password)

    else:
        raise_error(RESPONSES.ERRORS.VALIDATIONS.ADD_USER_VALIDATION_FAILED, message=user_serializer.errors)

    return user_serializer.data


# Update User Profile
def update_user(**body):

    filters = {"id": body['id']}
    user = user_db.get_user(**filters)

    if not user:
        raise_error(RESPONSES.USER.ERRORS.DOES_NOT_EXIST)

    user_serializer = UserSerializer(user, data=body, partial=True)

    if user_serializer.is_valid():
        user_serializer.save()
    else:
        raise_error(RESPONSES.ERRORS.VALIDATIONS.ADD_USER_VALIDATION_FAILED, message=user_serializer.errors)
        
    return user_serializer.data


def get_user_detail(**user):
    filters = {"id": user.get('user_id')}
    user = user_db.get_user(**filters)

    if not user:
        raise_error(RESPONSES.USER.ERRORS.DOES_NOT_EXIST)
    
    user_details = UserSerializer(user).data
    return user_details


# Login User
def login_user(**kwargs):
    
    user_filter = {"email": kwargs.get('email')}
    user = user_db.get_user(**user_filter)

    if not user:
        raise_error(RESPONSES.USER.ERRORS.INVALID_USER_EMAIL)
    
    user_password_filters = {"user_id": user.id}
   
    get_password = user_db.get_user_password(**user_password_filters)
   
    if not get_password:
        raise_error(RESPONSES.USER.ERRORS.INVALID_USER_PASSWORD)
    
    # check password validation
    password = kwargs.get("password")
    is_password_valid = check_password(password, get_password.password_hash)

    if is_password_valid:
        # Create jwt token with project detail
        jwt_token, refresh_token = user_utils.create_auth_token(user=user)
        response = {
                "access_token": jwt_token,
                "refresh_token": refresh_token
            }
    else:
        raise_error(RESPONSES.USER.ERRORS.INVALID_USER_PASSWORD)
    
    return response


def refresh_access_token(refresh_token):

    user_id = user_db.get_user_id_from_refresh_token(refresh_token=refresh_token)

    if not user_id:
        raise_error(RESPONSES.ERRORS.VALIDATIONS.INVALID_REFRESH_TOKEN)

    filters = {"id": user_id}
    user = user_db.get_user(**filters)

    if not user:
        raise_error(RESPONSES.USER.ERRORS.DOES_NOT_EXIST)

    jwt_token = user_utils.create_jwt_token(user=user)

    response = {
        "access_token": jwt_token
    }

    return response
 

def logout_user(**kwargs):
    refresh_token = kwargs.get('refresh_token')
    refresh_token_dict = {"token": refresh_token}
    user_db.expire_refresh_token(**refresh_token_dict)

    return True