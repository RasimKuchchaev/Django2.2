from django.urls import path
from app_pages.views import translation_example, greetings_page, welcome ,main_page
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('example/', translation_example, name='example'),
    path('greetings_page/', greetings_page, name='greetings_page'),
    # path('welcome/', cache_page(30)(welcome), name='welcome'),        # закеширована на 30сек тоже самое что и в view.py
    path('welcome/', welcome, name='welcome'),
    path('main_page/', main_page, name='main_page'),
]