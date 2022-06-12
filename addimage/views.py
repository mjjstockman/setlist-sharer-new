from django.shortcuts import render, redirect
from cloudinary.forms import cl_init_js_callbacks
from home.models import Gig
from .forms import AddImageForm






# Create your views here.

# DO SAME AS EDIT SETLIST BUT INCLUDE IMG UPLOAD FIELD
def add_image(request, pk):
    gig = Gig.objects.get(id=pk)
    # form = EditForm(instance=setlist)
    
    form = AddImageForm(request.POST, request.FILES, instance=gig)
    if request.method == 'POST':
        # form = EditForm(request.POST, instance=gig)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form,
    }
    return render(request, 'addimage/add-image.html', context)

# def add_image(request):
#     form = AddImageForm(request.POST, request.FILES)
#     if request.method == 'POST':
#         # form = AddImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')

#     # form = AddImageForm()
#     context = {'form': form}

#     return render(request, 'addimage/add_image.html', context)


    # def add_image(request):
    # form = AddImageForm(request.POST, request.FILES)
    # if request.method == 'POST':
        # form = AddImageForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('index')

    # context = {'form': form}

    # return render(request, 'addimage/add_image.html', context)