# Generated by Django 4.2.4 on 2023-08-21 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_library', '0005_author_birth_date_author_city_author_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('r', 'Review'), ('p', 'Published')], default='d', max_length=1),
        ),
    ]
