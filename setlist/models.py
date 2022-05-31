from django.db import models
from django.contrib.auth.models import User
from datetime import date
from home.models import Gig

STATUS = ((0, 'Waiting Confirmation'), (1, 'Published'))

# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)


    def __str__(self):
        return self.name

# class Gig(models.Model):
#     city = models.CharField(max_length=200)
#     date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
#     venue = models.ForeignKey(Venue, on_delete=models.CASCADE, null=True)


    # def __str__(self):
    #     return self.city


class Song(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True)

    def __str__(self):
        return self.title


class Release(models.Model):
    title = models.CharField(max_length=200)
    songs = models.ManyToManyField(Song, related_name="releases")
    slug = models.SlugField(max_length=200, unique=True, null=True)

    def __str__(self):
        return self.title


class Setlist(models.Model):
    gig = models.OneToOneField('home.Gig', on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    song = models.ManyToManyField(Song)
    status = models.IntegerField(choices=STATUS, default=0)
    agree = models.ManyToManyField(User, related_name='setlist_agree', blank=True)
    disagree = models.ManyToManyField(User, related_name='setlist_disagree', blank=True)
 


    def __str__(self):
        return f"{self.gig.venue} on {self.gig.date}"




