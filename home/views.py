from django.shortcuts import render
from setlist.models import Setlist
from .models import Gig


# Create your views here.

def gigs(request):
    gigs = Gig.objects.all().order_by('date')
    gigs_setlist_published = Setlist.objects.filter(status=1)
    gigs_setlist_pending = Setlist.objects.filter(status=0)
    gigs_no_setlist = Gig.objects.filter(setlist_gig__isnull=True)

    context = {
        'gigs': gigs,
        'published': gigs_setlist_published,
        'pending': gigs_setlist_pending,
        'no_list': gigs_no_setlist,
    }
    return render(request, 'index.html', context)