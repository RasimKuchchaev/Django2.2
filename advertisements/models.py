from django.db import models

# Create your models here.


class Advertisement(models.Model):
    title = models.CharField(max_length=1000)
