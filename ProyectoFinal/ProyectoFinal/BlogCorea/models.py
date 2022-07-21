from django.db import models

class Blogs(models.Model):
    imagen=models.ImageField()
    titulo=models.CharField(max_length=40)
    subtitulo=models.CharField(max_length=30)
    autor=models.CharField(max_length=30)
    fecha=models.DateTimeField()
    cuerpo=models.CharField(max_length=900)

class Cafes(models.Model):
    
