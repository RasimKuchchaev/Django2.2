from django.urls import path
from . import views
from .views import AdvertisementListView, AdvertisementDetailView
from django.views.generic.base import TemplateView


urlpatterns = [
    path("about/", views.About.as_view()),
    path("contacts/", views.contact_list, name='contact_list'),
    path("advertisements/", AdvertisementListView.as_view(), name='advertisements'),
    path("advertisements/<int:pk>", AdvertisementDetailView.as_view(), name='advertisement-detail')
]