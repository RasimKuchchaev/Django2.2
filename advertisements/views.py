from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

def advertisement_list(request, *args, **kwargs):
    advertisements = [
        'Мастер на час',
        'Ремонт компьютера',
        'Услуги сантехника'
    ]
    return render(request, 'advertisement/advertisements_list.html', {'advertisements': advertisements})

class About(View):
    def get(self, request):
        return render(request, 'advertisement/about.html',{'about':'about-qwerty'})



def contact_list(request, *args, **kwargs):
    contacts = [
        '01 - пожар',
        '02 - милиция',
        '03 - скорая',
        '04 - газ',
        '112 - SOS',
    ]
    return render(request, 'advertisement/contact.html', {'contacts': contacts})
