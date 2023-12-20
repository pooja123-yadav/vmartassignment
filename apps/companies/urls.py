from django.urls import path
import apps.companies.views as company_views

urlpatterns = [
    path("dropdown-list/", company_views.CompanyDropdownList.as_view(), name='get-company-dropdown'),
    path("list/", company_views.CompanyListWithDetails.as_view(), name='get-company-list'),
    path("create/", company_views.CreateCompany.as_view(), name='create-company')
]
