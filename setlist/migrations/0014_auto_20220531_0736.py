# Generated by Django 3.2 on 2022-05-31 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        ('setlist', '0013_auto_20220524_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setlist',
            name='gig',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.gig'),
        ),
        migrations.DeleteModel(
            name='Gig',
        ),
    ]