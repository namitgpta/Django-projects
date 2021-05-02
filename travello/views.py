from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.

def index(request):

    dests = Destination.objects.all()

    return render(request, 'index.html', {'year': 2021, 'dests':dests})