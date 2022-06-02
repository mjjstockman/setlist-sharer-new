from django.shortcuts import render
from .models import Gig
from setlist.models import Setlist

# Create your views here.

def gigs(request):
    gigs_setlist_published = Setlist.objects.filter(status=1)
    gigs_setlist_pending = Setlist.objects.filter(status=0)
    gigs_no_setlist = Gig.objects.filter(setlist_gig__isnull=True)

    context = {
        'published': gigs_setlist_published,
        'pending': gigs_setlist_pending,
        'no_list': gigs_no_setlist,
    }
    return render(request, 'index.html', context)