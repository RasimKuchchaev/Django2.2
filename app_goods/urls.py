from django.urls import path
from app_goods.views import items_list, update_prices, items_test

urlpatterns = [
    path('items/', items_list, name='item_list'),
    path('update_prices/', update_prices, name='update_prices'),
]