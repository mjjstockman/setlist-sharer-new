from django.db import models
from cloudinary.models import CloudinaryField
# from setlist.models import Setlist

# Create your models here.
class Gig(models.Model):
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    venue = models.ForeignKey('setlist.Venue', on_delete=models.CASCADE, null=True)
    featured_image = CloudinaryField('image', default='placeholder')


    def __str__(self):
        return f"{self.venue} in {self.venue.city} on {self.date}"


    

    