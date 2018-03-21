from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from .forms import ProgrammeForm, EventForm


def index(request):
    context = {'programmes':models.Programme.objects.all()} 

    return render(request, 'programme/home.html',context)


def add(request):
    if request.method=='POST':
        programmeForm = ProgrammeForm(request.POST)
        if programmeForm.is_valid():
            programmeForm.save()
        return HttpResponseRedirect('/programmes/')
    else:
        programmeForm = ProgrammeForm()
    
    context = {
        'form':programmeForm
        }
    return render(request, 'programme/add.html',context)

def delete(request, pk):
    models.Programme.objects.filter(pk=pk).delete()
    return HttpResponseRedirect('/programmes/')

#do auto fill programme field
def addEvent(request,pk):
    if request.method=='POST':
        eventForm = EventForm(request.POST)
        if eventForm.is_valid():
            eventForm.save()
        return HttpResponseRedirect('/programmes/')
    else:
        eventForm = EventForm()
    
    context = {
        'form':eventForm
        }
    return render(request, 'programme/add.html',context)