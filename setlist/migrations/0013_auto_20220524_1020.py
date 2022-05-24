# Generated by Django 3.2 on 2022-05-24 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0012_auto_20220520_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='song',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
    ]
