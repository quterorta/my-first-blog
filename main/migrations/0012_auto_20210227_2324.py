# Generated by Django 3.1.6 on 2021-02-27 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210227_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
    ]
