# Generated by Django 3.2 on 2022-06-13 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20220613_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gig',
            name='featured_image_status',
            field=models.IntegerField(choices=[(0, 'Waiting Confirmation'), (1, 'Published'), (3, 'No Image')], default=3),
        ),
    ]
