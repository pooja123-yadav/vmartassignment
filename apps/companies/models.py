from django.db import models

# Create your models here.

class Company(models.Model):
    class INDUSTRY_CHOICES (models.IntegerChoices):
        TECHNOLOGY = 1, 'Technology'
        FINANCE = 2, 'Finance'
        HEALTHCARE = 3, 'Healthcare'
        EDUCATION = 4, 'Education'
        OTHER = 5, 'Other'

    name         = models.CharField(max_length=255, null=False)
    industry     = models.IntegerField(choices=INDUSTRY_CHOICES.choices)   #constant
    description  = models.TextField(null=True, blank=True)
    founded_date = models.DateField(null=True, blank=True)
    website      = models.URLField(max_length=255, null=True, blank=True)
    location     = models.CharField(max_length=255, null=True, blank=True)
    logo_url     = models.CharField(max_length=255, null=True, blank=True)
    is_active    = models.BooleanField(default=True, db_index=True)
    is_deleted   = models.BooleanField(default=False, db_index=True)
    created      = models.DateTimeField(auto_now_add=True, db_index=True)
    updated      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'company'
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

