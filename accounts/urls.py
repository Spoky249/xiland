from django.urls import path
from . import views

urlpatterns=[
    path('singin' , views.singin , name='singin'),
    path('singup' , views.singup , name= 'singup'),
    path('profile', views.profile, name='profile'),

]