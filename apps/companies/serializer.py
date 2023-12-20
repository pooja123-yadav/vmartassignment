from rest_framework import serializers
from apps.companies.models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CompanyDropdownSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = ['id', 'name']  # Include only the necessary fields for the dropdown
