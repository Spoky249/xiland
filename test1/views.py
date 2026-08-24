from django.shortcuts import render
from django.http import HttpResponse    
# Create your views here.


def index (request):
    return HttpResponse('<h1>Django is working in spoky ha ha hvbvca  dvice ')

def my1(request):
    return HttpResponse('<h1>My first view in django</h1>')

def my2(request):
    return HttpResponse('<h1>my second page </h1>')

def my3(request):
    return HttpResponse('<h1>my third page </h1>')

