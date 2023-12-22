from django.db import models
from utils import date_time_utils
from django.conf import settings

# User model
class User(models.Model):
    
    class GENDER(models.IntegerChoices):
        MALE = 1, 'Male'
        FEMALE = 2, 'Female'
        OTHER = 3, 'Other'

    company_id      = models.PositiveIntegerField(db_index=True, null=False, blank=False)
    first_name      = models.CharField(max_length=50, null=False, blank=False)
    last_name       = models.CharField(max_length=50, null=False, blank=False)
    username        = models.CharField(max_length=255, unique=True)
    gender          = models.IntegerField(choices=GENDER.choices, default=GENDER.MALE, null=True, blank=True)
    country_code    = models.CharField(max_length=3, default="91")
    phone_number    = models.CharField(max_length=20, db_index=True)
    email           = models.EmailField(max_length=150, unique=True, null=False, blank=False, db_index=True)
    dob             = models.DateField(null=True, blank=True)
    image           = models.URLField(null=True, blank=True)
    is_active       = models.BooleanField(default=True, db_index=True)
    is_deleted      = models.BooleanField(default=False, db_index=True)
    created_by      = models.IntegerField(db_index=True, null=True)
    updated_by      = models.IntegerField(db_index=True, null=True)
    created         = models.DateTimeField(auto_now_add=True, db_index=True)
    updated         = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

# User Password model
class UserPassword(models.Model):
    
    user_id       = models.PositiveIntegerField(db_index=True, null=False, blank=False)
    password_hash = models.CharField(max_length=255, null=False, blank=False)
    expiry_date   = models.DateField(null=True)
    is_active     = models.BooleanField(default=True)
    created_by    = models.IntegerField(db_index=True, null=True)
    updated_by    = models.IntegerField(db_index=True, null=True)
    created       = models.DateTimeField(auto_now_add=True)
    updated       = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_password'
        verbose_name = 'User Password'
        verbose_name_plural = 'User Password'


class RefreshToken(models.Model):
    user_id     = models.PositiveIntegerField(db_index=True)  # Foreign key to user
    is_active   = models.BooleanField(default=True)
    token       = models.CharField(max_length=200, db_index=True)
    expiry_time = models.DateTimeField()
    created     = models.DateTimeField()
    updated     = models.DateTimeField()

    def __str__(self):
        return "%s, %s, %s" % (self.user_id, self.is_active, self.token)
    
    def save(self, *args, **kwargs):
        self.expiry_time = date_time_utils.add_days_to_datetime(
            date_time_utils.get_current_datetime(),
            settings.REFRESH_TOKEN_TIMEOUT)

    class Meta:
        db_table = 'refresh_token'



# class PasswordPolicy(models.Model):
#     attempts_allowed = models.IntegerField(null=True, blank=True)
#     time_between_attempts = models.CharField(max_length=10, null=True, blank=True)
#     policy_description = models.CharField(max_length=255, null=True, blank=True)
#     minimum_characters = models.CharField(max_length=2, null=True, blank=True)
#     block_duration = models.IntegerField(null=True, blank=True)
#     is_active = models.BooleanField(default=True)
#     created_by = models.IntegerField(db_index=True, null=True, blank=True)
#     updated_by = models.IntegerField(null=True, blank=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = 'password_policy'
#         verbose_name = 'Password Policy'
#         verbose_name_plural = 'Password Policy'
