# Generated by Django 3.2 on 2022-05-31 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
        ('setlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gig',
            name='venue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='setlist.venue'),
        ),
    ]