from apps.users.models import User, RefreshToken, UserPassword
from utils import date_time_utils
from rest_framework.exceptions import ValidationError


def get_user(**filters):
    if not filters.get('is_deleted'):
        filters.update({"is_deleted": False})
    user = User.objects.filter(**filters).first()
    return user


def save_refresh_token(**values):
    refresh_token = RefreshToken.objects.create(**values)
    return refresh_token


def save_user_password(**values):
    UserPassword.objects.create(**values)


def get_user_password(**filters):
    if not filters.get('is_active'):
        filters.update({"is_active": True})
    return UserPassword.objects.filter(**filters).first()


def expire_refresh_token(**refresh_token_dict):
    RefreshToken.objects.filter(**refresh_token_dict).update(is_active=0)


def get_user_id_from_refresh_token(refresh_token):
    
    current_datetime = date_time_utils.get_current_datetime()
    filters = {
        'token': refresh_token,
        'is_active': True,
        'expiry_time__gt': current_datetime
    }
    refresh_token = get_refresh_token(**filters)
    if refresh_token:
        return refresh_token.user_id
    else:
        return None
   
    
def get_refresh_token(**filters):
    try:
        refresh_token = RefreshToken.objects.get(**filters)
        return refresh_token
    except RefreshToken.DoesNotExist:
        raise ValidationError("Invalid refresh Token")
    except Exception as e:
        raise ValidationError("Invalid refresh Token")


