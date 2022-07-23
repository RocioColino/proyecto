from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns=[
    path('', views.inicio, name='inicio'),
    path('blogs/', views.blogs, name='blogs'),
    path('about/', views.about, name='about'),
    path('cafes/', views.cafes, name='cafes'),
    path('lugares/', views.lugares, name='lugares'),
    path('nuevoblog/', views.nuevoblog, name='nuevoblog'),
    path('nuevocafe/', views.nuevocafe, name='nuevocafe'),
    path('nuevolugar/', views.nuevolugar, name='nuevolugar'),
    path('busqueda_blog', views.busqueda_blog, name="busqueda_blog"),
    path('busqueda_cafe', views.busqueda_cafe, name="busqueda_cafe"), 
    path('busqueda_lugar', views.busqueda_lugar, name="busqueda_lugar"),    
]