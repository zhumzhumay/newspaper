# Generated by Django 4.1 on 2023-05-29 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='textauthor',
        ),
        migrations.AddField(
            model_name='post',
            name='text_author',
            field=models.CharField(default='', max_length=255, verbose_name='Автор статьи'),
        ),
    ]
