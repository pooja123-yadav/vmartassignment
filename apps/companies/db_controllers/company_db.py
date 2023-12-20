from apps.companies.models import Company


def get_list():
    list = Company.objects.values('id', 'name')
    return list

def get_list_with_detail():
    list = Company.objects.all()
    return list