from django.urls import path
from . import views

urlpatterns = [
    path('', views.gigs, name='index'),
    
]