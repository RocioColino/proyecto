from django.contrib import admin
from django.urls import path, include
from . import views


urlspatterns=[
    path('', views.inicio, name='inicio'),
    path('blogs/', views.blogs, name='blogs'),
    path('about/', views.about, name='about'),
    path('cafes/', views.cafes, name='cafes'),
    path('lugares/', views.lugares, name='lugares'),
    
]