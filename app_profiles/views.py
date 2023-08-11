from app_profiles.forms import UserForm
from django.views import View
from django.shortcuts import render

from app_profiles.models import User
from django.http import HttpResponseRedirect


class UserFormView(View):

    def get(self, request):
        user_form = UserForm()
        return render(request,'profiles/register.html', context={'user_form':user_form})

    def post(self, request):
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            # совершаем какую-то бизнес логику
            # к примеру сохранение в базу данных
            User.objects.create(**user_form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'profiles/register.html', context={'user_form': user_form})