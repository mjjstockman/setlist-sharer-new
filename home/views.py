from django.shortcuts import render
from setlist.models import Setlist
from .models import Gig
# from .forms import 

# Create your views here.

def gigs(request):
    gigs = Gig.objects.all().order_by('date')


    context = {
        'gigs': gigs,
    }
    return render(request, 'index.html', context)