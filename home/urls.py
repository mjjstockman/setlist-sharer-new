from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('create/', views.createSetlist, name='create-setlist'),
    # # path('create-setlist/', views.createSetlist, name='create-setlist'),
    # path('', views.setlist, name='setlist'),
    # path('update/<str:pk>/', views.updateSetlist, name='update-setlist'),
    # path('delete/<str:pk>/', views.deleteSetlist, name='delete-setlist'),
]