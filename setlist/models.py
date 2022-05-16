from django.db import models
from django.contrib.auth.models import User
from datetime import date

STATUS = ((0, 'Waiting Confirmation'), (1, 'Published'))

# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.name
        
class Gig(models.Model):
    city = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    # venue = 

    def __str__(self):
        return self.city


class Song(models.Model):
    title = models.CharField(max_length=200)
    # release =

    def __str__(self):
        return self.title

class Release(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Venue(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Setlist(models.Model):
    # gig = models.OneToOneField(Gig, on_delete=models.CASCADE, null=True)
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # song = models.ManyToManyField(Song)
    status = models.IntegerField(choices=STATUS, default=0)

    # def __str__(self):
    #     return self.gig.city

