from django.shortcuts import render
# from django.utils.translation import gettext
from django.utils.translation import gettext as _
from django.utils.formats import date_format, time_format
import datetime

def translation_example(request, *args, **kwargs):
    return render(request, "translation_example.html")


def greetings_page(request, *args, **kwargs):
    # greetings_message = gettext("Hello there! Today is %(date)s %(time)s") % {
    greetings_message = _("Hello there! Today is %(date)s %(time)s") % {
        'date': date_format(datetime.datetime.now().date(), format='SHORT_DATE_FORMAT', use_l10n=True),
        'time': time_format(datetime.datetime.now().time(), format='TIME_FORMAT', use_l10n=True)
    }
    return render(request, "greetings.html", context={
        'greetings_message': greetings_message
    })