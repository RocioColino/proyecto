from django.shortcuts import render, redirect
from django.http import HttpResponse
from BlogCorea.models import *
from ProyectoFinal.ProyectoFinal.BlogCorea.forms import NuevoBlog, NuevoCafe, NuevoLugar
#from . forms import *

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

def nuevoblog(request):
    if request.method=="POST":
        form=NuevoBlog(request.POST)
        if form.is_valid:
            form.save()
            return redirect('blogs')
    else:
        form=NuevoBlog()
    return render(request, 'BlogCorea/nuevoblog.html', {"form":form})

def busqueda_blog(request):
    if request.method=="POST":
        blogs=request.POST["nombre"]
        resultado=Blogs.objects.filter(nombre__icontains=blogs)
        return render(request, "BlogCorea/busqueda_blog.html", {"blogs":resultado})
    return render(request, "BlogCorea/busqueda_blog.html", {})


def nuevocafe(request):
    if request.method=="POST":
        form=NuevoCafe(request.POST)
        if form.is_valid:
            form.save()
            return redirect('cafes')
    else:
        form=NuevoCafe()
    return render(request, 'BlogCorea/nuevocafe.html', {"form":form})

def busqueda_cafe(request):
    if request.method=="POST":
        cafes=request.POST["nombre"]
        resultado=Cafes.objects.filter(nombre__icontains=cafes)
        return render(request, "BlogCorea/busqueda_cafes.html", {"cafes":resultado})
    return render(request, "BlogCorea/busqueda_cafes.html", {})

def nuevolugar(request):
    if request.method=="POST":
        form=NuevoLugar(request.POST)
        if form.is_valid:
            form.save()
            return redirect('lugares')
    else:
        form=NuevoLugar()
    return render(request, 'BlogCorea/nuevolugar.html', {"form":form})

def busqueda_lugar(request):
    if request.method=="POST":
        lugares=request.POST["nombre"]
        resultado=Lugares.objects.filter(nombre__icontains=lugares)
        return render(request, "BlogCorea/busqueda_lugares.html", {"lugares":resultado})
    return render(request, "BlogCorea/busqueda_lugares.html", {})
