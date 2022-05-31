from django.db import models
# from setlist.models import Setlist

# Create your models here.
class Gig(models.Model):
    city = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    venue = models.ForeignKey('setlist.Venue', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.city