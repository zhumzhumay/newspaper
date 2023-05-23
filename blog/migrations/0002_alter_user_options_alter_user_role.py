# Generated by Django 4.1 on 2023-05-23 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(choices=[(1, 'Суперпользователь'), (2, 'Новостной редактор'), (3, 'Читатель')], default=3, verbose_name='Роль'),
        ),
    ]
