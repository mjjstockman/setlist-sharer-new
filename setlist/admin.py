from django.contrib import admin
from . models import Gig, Song, Setlist, Venue

# Register your models here.
admin.site.register(Gig)
admin.site.register(Song)
admin.site.register(Setlist)
admin.site.register(Venue)