from django.contrib.auth.hashers import check_password, make_password
from apps.users.db_controllers import user_db
from rest_framework.exceptions import ValidationError
from apps.users.serializer import UserSerializer


# Login User
def login_user(**kwargs):
    
    filters = {"email": kwargs.get('email')}
    user = user_db.get_user(**filters)

    if not user:
        raise ValidationError("User not found")
    
    # check password validation
    password = kwargs.get("password")
    is_password_valid = check_password(password, user.password)

    if is_password_valid:
        # generate jwt token and referesh token
        pass
    else:
        raise ValidationError("Invalid Password")
    

# Create a User
def create_user(body, token_payload):
    raw_password = body.get('password')

    body['password'] = make_password(body.get('password'))

    user_serializer = UserSerializer(data=body)


    if user_serializer.is_valid():

        user_instance = user_serializer.save()
        
    return user_serializer.data


# Update User Profile
def update_user(body, token_payload):

    filters = {"id": body['user_id']}
    user = user_db.get_user(**filters)

    if not user:
        raise ValidationError("User not found")

    user_serializer = UserSerializer(user, data=body, partial=True)

    if user_serializer.is_valid():
        user_serializer.save()
        
    return user_serializer.data

    
