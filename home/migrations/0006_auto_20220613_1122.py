# Generated by Django 3.2 on 2022-06-13 11:22

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20220613_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gig',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='gig',
            name='featured_image_status',
            field=models.IntegerField(choices=[(0, 'Waiting Confirmation'), (1, 'Published')], default=0),
        ),
    ]
