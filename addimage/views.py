from django.shortcuts import render, HttpResponse

# Create your views here.
def safe(request):
    return HttpResponse('safe')