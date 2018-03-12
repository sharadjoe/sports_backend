from django.shortcuts import render
from django.http import HttpResponse
from . import models
def index(request):

    return render(request, 'programme/home.html', {'programmes':models.Programme.objects.all()})