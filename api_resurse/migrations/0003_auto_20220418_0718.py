# Generated by Django 3.0.5 on 2022-04-17 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_resurse', '0002_auto_20220417_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='genres',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
