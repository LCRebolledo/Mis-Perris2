from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from adopciones.models import Mascotas, Perfiles


class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascotas
        fields =[
            'nombre',
            'raza',
            'estado',
            'descripcion',
            'imagen',
            ]
        
        labels = {
            'nombre':'Nombre',
            'raza': 'Raza',
            'estado':'Estado',
            'descripcion':'Descripción mascota',
            'imagen':'Foto de la mascota'
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'raza':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
        }


class RegForm(forms.Form):

    nombres = forms.CharField(max_length=100)
    apellidos = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    rut = forms.CharField()
    telefono = forms.IntegerField()
 

class MForm(forms.Form):

    nombre = forms.CharField(max_length=100)
    raza = forms.CharField()
    estado = forms.CharField()
    descripcion = forms.CharField()
    imagen = forms.ImageField()




        