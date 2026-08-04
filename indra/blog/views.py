from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): 
    return HttpResponse("<h1> Hello my name is indra</h1>")

def about(request): 
    return HttpResponse("<h1> Hello my name is about</h1>")
