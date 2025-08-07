from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('even_odd/', views.even_odd),
    path('file/', views.file),
]
