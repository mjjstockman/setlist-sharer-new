from django.shortcuts import render
from .models import Gig

# Create your views here.
# def index(request):
#     return render(request, 'index.html')

def gigs(request):
    # setlists = Setlist.objects.filter(status=1)
    gigs = Gig.objects.all()
    context = {
        # 'setlists': setlists,
        'gigs': gigs,
    }
    return render(request, 'index.html', context)