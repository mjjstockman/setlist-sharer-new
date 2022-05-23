from django.contrib import admin
from . models import Gig, Song, Setlist, Venue, Release

# Register your models here.
admin.site.register(Gig)
admin.site.register(Song)

admin.site.register(Venue)
admin.site.register(Release)


class SetlistAdmin(admin.ModelAdmin):
    list_display = ('gig', 'status', 'author')

admin.site.register(Setlist, SetlistAdmin)