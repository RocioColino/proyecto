from django.shortcuts import render, redirect
from django.http import HttpResponse
from BlogCorea.models import *
from . forms import *

def inicio(request):
    return render(request, 'BlogCorea/index.html', {})

def about(request):
    return render (request, 'BlogCorea/about.html', {})



def blogs(request):
    blogs=Blogs.objects.all()
    return render(request, 'BlogCorea/blogs.html', {"blogs":blogs})

def cafes(request):
    cafes=Cafes.objects.all()
    return render(request, 'BlogCorea/cafes.html', {"cafes":cafes})

def lugares(request):
    lugares=Lugares.objects.all()
    return render(request, 'BlogCorea/lugares.html', {"lugares":lugares})







