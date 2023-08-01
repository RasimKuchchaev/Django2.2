from django.shortcuts import render


def advertisement_list(request, *args, **kwargs):
    advertisements = [
        'Мастер на час',
        'Ремонт компьютера',
        'Услуги сантехника'
    ]
    return render(request, 'advertisement/advertisements_list.html', {'advertisements': advertisements})


def contact_list(request, *args, **kwargs):
    contacts = [
        '01 - пожар',
        '02 - милиция',
        '03 - скорая',
        '04 - газ',
        '112 - SOS',
    ]
    return render(request, 'advertisement/contact.html', {'contacts': contacts})
