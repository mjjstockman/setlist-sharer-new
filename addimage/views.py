from django.shortcuts import render, redirect
from .forms import AddImageForm
from cloudinary.forms import cl_init_js_callbacks




# Create your views here.
def add_image(request):
    form = AddImageForm(request.POST, request.FILES)
    if request.method == 'POST':
        # form = AddImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    # form = AddImageForm()
    context = {'form': form}

    return render(request, 'addimage/add_image.html', context)