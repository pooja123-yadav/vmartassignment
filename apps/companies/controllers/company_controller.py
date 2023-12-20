from apps.companies.db_controllers import company_db
from apps.companies.serializer import CompanySerializer, CompanyDropdownSerializer

def get_dropdown_list():
    company_list = company_db.get_list()
    serializer = CompanyDropdownSerializer(company_list, many=True)
    return serializer.data

def get_company_detail_list():
    company_list = company_db.get_list_with_detail()
    serializer = CompanySerializer(company_list, many=True)
    return serializer.data

def create_company():
    company_list = company_db.get_list_with_detail()
    serializer = CompanySerializer(company_list, many=True)
    return serializer.data
