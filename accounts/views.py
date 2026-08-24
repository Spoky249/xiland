from django.shortcuts import render

# Create your views here.


def singin(request):
    return render( request , 'accounts/singin.html')


def singup(request):
    return render( request , 'accounts/singup.html')

def profile(request):
    return render( request , 'accounts/profile.html')