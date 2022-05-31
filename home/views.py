from django.shortcuts import render
from .models import Gig

# Create your views here.

def gigs(request):

    gigs = Gig.objects.all()
    context = {
        'gigs': gigs,
    }
    return render(request, 'index.html', context)