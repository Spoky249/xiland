from django.shortcuts import render
from django.contrib import messages

# Create your views here.


def singin(request):
    if request.GET:
        messages.info(request, 'Testing messages 1')
        messages.success(request, 'Testing messages 2')
        messages.warning(request, 'Testing messages 3')
        messages.error(request, 'Testing messages 4')
    return render( request , 'accounts/singin.html')


def singup(request):
    messages.error(request, 'Testing messages 4')
    return render( request , 'accounts/singup.html')

def profile(request):
    return render( request , 'accounts/profile.html')