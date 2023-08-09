from django.db import models

# Create your models here.


class Advertisement(models.Model):
    title = models.CharField(max_length=1000, verbose_name='Заголовок')
    description = models.CharField(max_length=1000, default='', verbose_name='Описание')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(default=0, verbose_name='цена')
    view_count = models.IntegerField(default=0, verbose_name='количество просмотров')
    status = models.ForeignKey('AdvertisementStatus', on_delete=models.CASCADE, default=None, null=True, verbose_name='Статус')


    def __str__(self):
        return self.title

    class Meta:
        db_table = 'advertisement'
        ordering = ['title']


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name