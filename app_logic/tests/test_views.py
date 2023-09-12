from django.test import TestCase
from django.urls import reverse


class WelcomePageTest(TestCase):
    def test_welcome_page(self):
        url = reverse('welcome')        # name url получаем страницу
        response = self.client.get(url)             # client - простой браузер
        self.assertEqual(response.status_code, 200)           # Странице доступна
        self.assertContains(response, 'Добро пожаловать!')      # На странице есть текст Добро пожаловать!