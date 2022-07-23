from django import forms
from .models import *

class NuevoBlog(forms.ModelForm):
    class Meta: 
        model=Blogs
        fields='__all__'


class NuevoCafe(forms.ModelForm):
    class Meta:
        model=Cafes
        fields='__all__'   

class NuevoLugar(forms.ModelForm):
    class Meta:
        model=Lugares
        fields='__all__'
