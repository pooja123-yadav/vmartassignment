from django.db import models

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
    email           = models.EmailField(max_length=150, null=True, blank=True, db_index=True)
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
    
    user_id       = models.PositiveIntegerField(db_index=True)
    password_hash = models.CharField(max_length=255)
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

    