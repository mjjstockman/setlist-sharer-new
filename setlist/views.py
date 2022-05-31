from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Setlist
from home.models import Gig
from .forms import SetlistForm, EditForm


def agree(request, pk):
    setlist = Setlist.objects.get(id=pk)
    disagree = False

    for disagree in setlist.disagree.all():
        if disagree == request.user:
            disagree = True
            break

    if disagree:
        setlist.disagree.remove(request.user)

    agree = False

    for agree in setlist.agree.all():
        if agree == request.user:
            agree = True
            break
        
    if not agree:
        setlist.agree.add(request.user)

    if agree:
        setlist.agree.remove(request.user)

    return redirect(request.META['HTTP_REFERER'])


def disagree(request, pk):
    setlist = get_object_or_404(Setlist, id=request.POST.get('setlist_id'))

    agree = False

    for agree in setlist.agree.all():
        if agree == request.user:
            agree = True
            break

    if agree:
        setlist.agree.remove(request.user)

    disagree = False

    for disagree in setlist.disagree.all():
        if disagree == request.user:
            disagree = True
            break
        
    if not disagree:
        setlist.disagree.add(request.user)

    # change to else??
    if disagree:
        setlist.disagree.remove(request.user)

    return redirect(request.META['HTTP_REFERER'])




@login_required
def setlist_detail(request, pk):
    setlist = Setlist.objects.get(id=pk)
    context = {
        'setlist': setlist,
    }
    return render(request, 'setlist/setlist-detail.html', context)


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
    form = EditForm(instance=setlist)
    

    if request.method == 'POST':
        form = EditForm(request.POST, instance=setlist)
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