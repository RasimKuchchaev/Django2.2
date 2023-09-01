from django.db import models


class File(models.Model):
    file = models.FileField(upload_to='files/')
    description = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)