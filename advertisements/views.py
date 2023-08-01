from django.shortcuts import render
from django.http import HttpResponse


def advertisement_list(request, *args, **kwargs):
    advertisements = [
        'Мастер на час',
        'Ремонт компьютера',
        'Услуги сантехника'
    ]
    return render(request, 'advertisement/advertisements_list.html', {'advertisements':advertisements})


