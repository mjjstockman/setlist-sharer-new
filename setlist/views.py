from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Setlist, Gig
from .forms import SetlistForm


def agree(request, pk):
    # get relevant setlist id
    # setlist = get_object_or_404(Setlist, id=request.POST.get('setlist_id'))
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
    #  'setlist/setlists.html')
    # return redirect(request.path)
    # return HttpResponseRedirect(request.path_info)

    # next = request.POST.get('next', '/')
    # return HttpResponseRedirect(next)

    # if setlist.agree.filter(id=request.user.id).exists():
    #     setlist.agree.remove(request.user)
    # else:
    #     setlist.agree.add(request.user)
    # return render(request, 'setlist/setlists.html')


def disagree(request, pk):
    # get relevant setlist id
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

def all(request):
    setlists = Setlist.objects.filter(status=1)
    gigs = Gig.objects.all()
    context = {
        'setlists': setlists,
        'gigs': gigs,
    }
    return render(request, 'setlist/setlists.html', context)


def setlist_detail(request, pk):
    # setlists = Setlist.objects.filter(status=1)
    setlist = Setlist.objects.get(id=pk)
    # gigs = Gig.objects.all()
    context = {
        'setlist': setlist,
        # 'gigs': gigs,
    }
    return render(request, 'setlist/setlist-detail.html', context)


# def edit(request, pk):
#     setlist = Setlist.objects.get(id=pk)
#     form = SetlistForm(instance=setlist)

#     if request.method == 'POST':
#         form = SetlistForm(request.POST, instance=setlist)
#         if form.is_valid():
#             form.save()
#             return redirect('/')

#     context = {
#         'form': form,
#     }
#     return render(request, 'setlist/add.html', context)

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