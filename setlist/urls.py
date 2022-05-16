# from django.contrib import admin
from django.urls import path
from .views import add

urlpatterns = [
    # path('', get_setlists, name='setlist'),
    path('add/', add, name='add_setlist'),
    # path('edit/<str:pk>/', edit, name='edit_setlist'),
    # path('delete/<str:pk>/', delete, name='delete_setlist'),
]