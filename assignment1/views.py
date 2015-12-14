from django.shortcuts import render

 # views.py impl
from django.http import HttpResponse
""""def hello(request):
    return HttpResponse("Deneme")"""

def say(request,x):
    reader = open(x)
    words = reader.read().splitlines()

    dictt = {reader:x.count(t) for t in x}
    return HttpResponse(dictt)


# Create your views here.
