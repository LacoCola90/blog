# Generated by Django 3.2.9 on 2021-11-09 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorozatplanetblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default=models.CharField(max_length=255), max_length=255),
        ),
    ]
