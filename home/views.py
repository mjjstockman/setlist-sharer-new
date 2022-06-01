from django.shortcuts import render
from .models import Gig
from setlist.models import Setlist

# Create your views here.

def gigs(request):

    gigs = Gig.objects.all()

    gigs_setlist_published = Setlist.objects.get(status=1)
    # gigs_setlist_pending = Gig.objects.filter(status=0)
   
    context = {
        'published': gigs_setlist_published,
        # 'pending': gigs_setlist_pending,
        'gigs': gigs,
    }
    return render(request, 'index.html', context)