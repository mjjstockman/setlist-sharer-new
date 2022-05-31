# from django.contrib import admin
from django.urls import path
from home.views import gigs
from .views import add, edit, delete, agree, disagree, setlist_detail


urlpatterns = [
    path('', gigs, name='gigs'),
    path('add/<int:pk>/', add, name='add_setlist'),
    path('edit/<str:pk>/', edit, name='edit_setlist'),
    path('delete/<str:pk>/', delete, name='delete_setlist'),
    path('agree/<str:pk>/', agree, name='agree'),
    path('disagree/<str:pk>/', disagree, name='disagree'),
    path('setlist-detail/<str:pk>/', setlist_detail, name='detail'),
]