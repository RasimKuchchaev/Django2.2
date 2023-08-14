from django import forms
import datetime
from django.core.exceptions import ValidationError


class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    first_name = forms.CharField()
    second_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    birthday = forms.DateField()

    def clean_birthday(self):       # фильтрация по 1 полю
        data = self.cleaned_data['birthday']
        today = datetime.date.today()
        year_delta = (today-data).days / 365
        if year_delta < 18:
            raise ValidationError('Регистрироватся могут лица 18+')
        return data

    def clean(self):        # фильтрация по 2 и более полям
        cleaned_data = super(UserForm, self).clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if first_name=='Ivan' and last_name=='Ivanov':
            msg = 'Запрещено регистрироватся'
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)


    """
    python manage.py shell
    Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>> from app_profiles.forms import UserForm
    >>> incorect_user = {'username': 'Alex', 'password': 'paswordAlex', 'first_name': 'Ivan', 'second_name': 'Alex', 'last_name': 'Ivanov', 'email': 'Alex@mail.ru', 'birthday': '2001-01-01'}
    >>> user_form = UserForm(incorect_user)
    >>> user_form.is_valid()
    False
    >>> user_form.errors
    {'first_name': ['Запрещено регистрироватся'], 'last_name': ['Запрещено регистрироватся']}
    >>>
    >>> user_form.cleaned_data
    {'username': 'Alex', 'password': 'paswordAlex', 'second_name': 'Alex', 'email': 'Alex@mail.ru', 'birthday': datetime.date(2001, 1, 1)}
    """