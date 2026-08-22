from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    return HttpResponse('<h1>Django is working in spoky ha ha ha  dvice ')

def my1(requesty):
    return HttpResponse('<h1>my first from test2 </h1>')