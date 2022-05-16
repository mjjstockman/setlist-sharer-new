from django.shortcuts import render, redirect
from .forms import SetlistForm


def add(request):
    form = SetlistForm()
    # if request.method == 'POST':
    #     form = SetlistForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('')

    context = {
        'form': form
    }
    return render(request, 'add.html', context)
