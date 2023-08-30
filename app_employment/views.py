from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from app_employment.models import Vacancy


# def vacancy_list(request):
#     # if request.user.has_perm('app_employment.view_vacancy'):    # <app>.<action>_<object_name>
#     #     vacancies = Vacancy.objects.all()
#     #     return render(request, 'employment/vacancy_list.html', {'vacancy': vacancies})
#     # else:
#     #     raise PermissionDenied()
#
#     if not request.user.has_perm('app_employment.view_vacancy'):    # <app>.<action>_<object_name>
#         raise PermissionDenied()
#     vacancies = Vacancy.objects.all()
#     return render(request, 'employment/vacancy_list.html', {'vacancy_list': vacancies})


@permission_required('app_employment.view_vacancy')
def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'employment/vacancy_list.html', {'vacancy_list': vacancies})