from django.contrib import admin
from . models import Gig, Song, Setlist, Venue, Release

# Register your models here.
admin.site.register(Gig)


admin.site.register(Venue)



class SetlistAdmin(admin.ModelAdmin):
    list_display = ('gig', 'status', 'author')
    actions = ['approve_setlist']

    def approve_setlist(self, request, queryset):
        queryset.update(status=True)
    

admin.site.register(Setlist, SetlistAdmin)

class SongAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class ReleaseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Song, SongAdmin)
admin.site.register(Release, ReleaseAdmin)