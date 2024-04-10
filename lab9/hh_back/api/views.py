from django.http import JsonResponse, Http404
from api.models import Vacancy, Company

def company_list(request):
    companies = Company.objects.all()
    companies_json = [c.to_json() for c in companies]
    return JsonResponse(companies_json, safe=False)

def company_detail(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist:
        raise Http404("This company does not exist")
    return JsonResponse(company.to_json(), safe=False)

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [v.to_json() for v in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def vacancy_detail(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist:
        raise Http404("This vacancy does not exist")
    return JsonResponse(vacancy.to_json(), safe=False)

def vacancy_top_ten(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    vacancies_json = [v.to_json() for v in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def company_vacancy_list(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist:
        raise Http404("This company does not exist")
    vacancies = Vacancy.objects.filter(company=company)
    vacancies_json = [v.to_json() for v in vacancies]
    return JsonResponse(vacancies_json, safe=False)
