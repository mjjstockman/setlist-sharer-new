# Generated by Django 3.2 on 2022-05-16 16:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('setlist', '0004_release_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='setlist',
            name='gig',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='setlist.gig'),
        ),
        migrations.AddField(
            model_name='setlist',
            name='song',
            field=models.ManyToManyField(to='setlist.Song'),
        ),
        migrations.AddField(
            model_name='setlist',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]