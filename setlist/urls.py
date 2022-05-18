# from django.contrib import admin
from django.urls import path
from .views import all, add, edit, delete, agree

urlpatterns = [
    path('', all, name='setlist'),
    path('add/', add, name='add_setlist'),
    path('edit/<str:pk>/', edit, name='edit_setlist'),
    path('delete/<str:pk>/', delete, name='delete_setlist'),
    path('agree/<str:pk>/', agree, name='agree'),
]