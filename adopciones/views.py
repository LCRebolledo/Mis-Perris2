from django.utils import timezone
from .models import*
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView 
from django.contrib.auth.views import LoginView
from .forms import MascotaForm, RegForm, MForm

        
def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('guarda_mascota')
    else:
        form = MascotaForm()

    return render(request, 'adopcion/form_mascota.html', {'form':form})


def mascota_lista(request):
    mascota = Mascotas.objects.all()
    return render(request,'adopcion/ListaMascotas.html', {'mascota': mascota})



def Main_list (request):
    return render(request,'adopcion/Main.html')


def Form_list (request):
    return render(request,'adopcion/formularioo.html')

def Somos_list (request):
    return render(request,'adopcion/campania.html')


class BienvenidaView(TemplateView):
   template_name = 'perfiles/bienvenida.html'

class SignInView(LoginView):
   template_name = 'adopcion/sesion.html'
   

class SignOutView(LogoutView):
    pass


def registrar_list(request):
    form = RegForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        form_data = form.cleaned_data
        email = form_data.get("email")
        rut = form_data.get("rut")
        tele = form_data.get("telefono")
        name = form_data.get("nombres")
        last_name = form_data.get("apellidos")
        obj = Registrado.objects.create(
        nombres=name,
        apellidos=last_name,    
        email=email, 
        rut=rut, 
        telefono=tele)
        
    return render(request, 'adopcion/formularioo.html', context)

    def __str__(self):
        return self.email

def registrar_mascota(request):
    form = MForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        form_data = form.cleaned_data
        nombre = form_data.get("nombre")
        raza = form_data.get("raza")
        estado = form_data.get("estado")
        descripcion = form_data.get("descripcion")
        foto = form_data.get("imagen")
        obj = Registrado.objects.create(
        nombre=nombre,
        raza=raza,    
        estado=estado, 
        descripcion=descripcion, 
        foto=imagen)
        
    return render(request, 'adopcion/formulariomascota.html', context)

    def __str__(self):
        return self.email

