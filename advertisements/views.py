from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from advertisements.models import Advertisement


def advertisement_list(request, *args, **kwargs):
    advertisements = Advertisement.objects.all()
    return render(request, 'advertisement/advertisements.html', {
        'advertisements': advertisements
    })

class About(TemplateView):
    template_name = 'advertisement/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Бесплатные обьявления в вашем городе'
        context['title'] = 'Бесплатные обьявления'
        context['description'] = """
            Господа, граница обучения кадров прекрасно подходит для реализации новых принципов формирования 
            материально-технической и кадровой базы. В частности, постоянный количественный рост и сфера нашей 
            активности позволяет оценить значение как самодостаточных, так и внешне зависимых концептуальных решений. 
            Однозначно, тщательные исследования конкурентов описаны максимально подробно. Безусловно, существующая 
            теория предопределяет высокую востребованность системы массового участия. Господа, социально-экономическое 
            развитие предполагает независимые способы реализации существующих финансовых и административных условий.
        """
        return context


def contact_list(request, *args, **kwargs):
    contacts = [
        '01 - пожар',
        '02 - милиция',
        '03 - скорая',
        '04 - газ',
        '112 - SOS',
    ]
    return render(request, 'advertisement/contact.html', {'contacts': contacts})
