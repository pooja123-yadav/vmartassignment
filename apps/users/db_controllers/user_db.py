from apps.users.models import User


def get_user(**filters):
    user = User.non_deleted_objects.filter(**filters).first()
    return user