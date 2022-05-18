from django.shortcuts import render, redirect, get_object_or_404
# from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Setlist
from .forms import SetlistForm


def agree(request, pk):
    setlist = get_object_or_404(Setlist, id=request.POST.get('setlist_id'))
    setlist.agree.add(request.user)
    return render(request, 'setlist/setlists.html')


def all(request):
    setlists = Setlist.objects.filter(status=1)
    context = {
        'setlists': setlists,
    }
    return render(request, 'setlist/setlists.html', context)


def add(request):
    form = SetlistForm()
    if request.method == 'POST':
        form = SetlistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'setlist/add.html', context)


def edit(request, pk):
    setlist = Setlist.objects.get(id=pk)
    form = SetlistForm(instance=setlist)

    if request.method == 'POST':
        form = SetlistForm(request.POST, instance=setlist)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form,
    }
    return render(request, 'setlist/add.html', context)


def delete(request, pk):
    setlist = Setlist.objects.get(id=pk)

    if request.method == 'POST':
        setlist.delete()
        return redirect('/')
        
    context = {
        'setlist': setlist,
    }
    return render(request, 'setlist/delete.html', context)