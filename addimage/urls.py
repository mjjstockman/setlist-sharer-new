# from django.contrib import admin
from django.urls import path
from home.views import gigs
from .views import safe


urlpatterns = [
    # url user types in, view function to return, name
    path('', safe, name='safe'),
]