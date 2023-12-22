from utils import date_time_utils
from django.conf import settings
import jwt, uuid
from apps.users.db_controllers import user_db


def create_auth_token(user):
    jwt_token = create_jwt_token(user=user)

    unique_id = uuid.uuid4()

    refresh_token = create_refresh_token(token=unique_id, user_id=user.id)

    return jwt_token, refresh_token


def create_jwt_token(user=None):
    
    current_datetime = date_time_utils.get_current_datetime()
    jwt_expiry_time = date_time_utils.add_minutes_to_datetime(current_datetime, settings.JWT_EXPIRY_DURATION)
    
    jwt_expiry_time = int(jwt_expiry_time.timestamp())

    token_payload = {
        'exp': jwt_expiry_time,
        "user_details": {
            "company_id": user.company_id if user and user.company_id else None,
            'user_id': user.id if user and user.id else None,
            'name': f"{user.first_name or ''} {user.last_name or ''}".strip(),
            'email': user.email if user and user.email else '',
            'phone_number': user.phone_number if user and user.phone_number else None,
        } 
    }
    token = jwt.encode(token_payload, settings.JWT_SECRET_KEY, algorithm='HS256')
    return token


def create_refresh_token(token, user_id):
    values = {"token": token, "user_id": user_id, "is_active": True}
    refresh_token = user_db.save_refresh_token(**values)
    return refresh_token.token


# def authenticate_jwt_token(jwt_token):
#     if not jwt_token:
#         raise_error(RESPONSES.GENERIC.UNAUTHORIZED)

#     try:
#         payload = jwt.decode(jwt_token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
       
#         current_datetime = date_time_utils.get_current_datetime()
#         current_datetime = int(current_datetime.timestamp())
#         expiry = payload['exp']
       
#         if current_datetime > expiry:
#             raise_error(RESPONSES.GENERIC.UNAUTHORIZED)
#         return payload
#     except Exception as e:
#         raise_error(RESPONSES.GENERIC.UNAUTHORIZED)
