# Generated by Django 4.0.4 on 2022-05-03 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(default='', help_text='Максимум 250 символів', max_length=250, verbose_name='Slug'),
        ),
    ]
