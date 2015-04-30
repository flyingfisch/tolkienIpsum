from django.shortcuts import render
from django.http import HttpResponse
from .logic import *

def index(request):
    return HttpResponse(GenerateIpsum(10))
#    return render(request, 'generator/index.html', {'request_id': request_id})
