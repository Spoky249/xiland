from django.shortcuts import render
from django.contrib import messages

# Create your views here.


def singin(request):
    if request.method == 'GET':
        messages.info(request, 'Testing messages 1')
    return render( request , 'accounts/singin.html')


def singup(request):
    return render( request , 'accounts/singup.html')

def profile(request):
    return render( request , 'accounts/profile.html')