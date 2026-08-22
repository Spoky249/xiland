from django.urls import path
from . import views
urlpatterns=[
    path(''    , views.index, name='index'),
    path('my1',views.my1,name='my1')
]