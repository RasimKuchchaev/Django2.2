from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    genre = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=50)
    is_active = models.BooleanField()

