# Generated by Django 3.1.6 on 2021-02-27 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210227_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='website',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='news',
            name='author_avatar',
            field=models.ImageField(default='bgmt-logo-minimal.png', upload_to='', verbose_name='Фото автора'),
        ),
    ]
