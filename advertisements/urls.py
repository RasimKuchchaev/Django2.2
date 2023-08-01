from django.urls import path
from . import views


urlpatterns = [
    path("", views.advertisement_list, name='advertisement_list'),
    path("about/", views.About.as_view()),
    path("contacts/", views.contact_list, name='contact_list')
]