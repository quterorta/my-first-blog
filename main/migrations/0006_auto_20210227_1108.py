# Generated by Django 3.1.6 on 2021-02-27 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210227_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='author_avatar',
            field=models.ImageField(default="{% static 'main/img/logo-minimal.png' %}", upload_to='', verbose_name='Фото автора'),
        ),
    ]
