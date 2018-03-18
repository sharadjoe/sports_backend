from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from .forms import ProgrammeForm


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


