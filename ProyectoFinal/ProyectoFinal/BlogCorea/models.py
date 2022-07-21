from django.db import models

class Blogs(models.Model):
    imagen=models.ImageField()
    titulo=models.CharField(max_length=40)
    subtitulo=models.CharField(max_length=30)
    autor=models.CharField(max_length=30)
    fecha=models.DateTimeField()
    cuerpo=models.CharField(max_length=900)

class Cafes(models.Model):
    nombre=models.CharField(max_length=30)
    precio=models.CharField(max_length=10)
    imagen=models.ImageField()
    direccion=models.CharField(max_length=40)
    telefono=models.IntegerField()

class Lugares(models.Model):
    nombre=models.CharField(max_length=30)
    imagen=models.ImageField()
    descripcion=models.CharField(max_length=200)
    direccion=models.CharField(max_length=50)
    telefono=models.IntegerField()

