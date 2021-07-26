from django.shortcuts import render
from django.http import HttpResponse

from .tasks import sleepy

# Create your views here.

def index(request):
    return HttpResponse('<h1>Email has sent!</h1>')



