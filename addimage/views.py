from django.shortcuts import render

# Create your views here.
def add_image(request):
    return render(request, 'addimage/add_image.html')