from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Clock

# Create your views here.

def index(request):
    time_left = Clock.timediff
    return render(request, 'brexittime/index.html', {
        'time_left': time_left
    })

    
