# from django.contrib import admin
from django.urls import path
from home.views import gigs
from .views import add_image


urlpatterns = [
    # url user types in, view function to return, name
    path('', add_image, name='add-image'),
]