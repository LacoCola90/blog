# Generated by Django 3.2.9 on 2021-11-16 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorozatplanetblog', '0007_post_snippet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(max_length=255),
        ),
    ]