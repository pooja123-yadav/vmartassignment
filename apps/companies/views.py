from rest_framework.views import APIView
from utils.responses import prepare_response, RESPONSES
from apps.companies.controllers import company_controller


class CompanyDropdownListAPI(APIView):
    def get(self, request):
        response = company_controller.get_dropdown_list()
        return prepare_response(RESPONSES.GENERIC.SUCCESS, data=response)


class CompanyListWithDetailsAPI(APIView):
    def get(self, request):
        response = company_controller.get_company_detail_list()
        return prepare_response(RESPONSES.GENERIC.SUCCESS, data=response)
 
    
class CreateCompanyAPI(APIView):
    def post(self, request):
        body = request.data
        response = company_controller.create_company(**body)
        return prepare_response(RESPONSES.GENERIC.SUCCESS, data=response)

