from django.shortcuts import render, redirect
from .models import Persona

# Create your views here.
def home(request):
    registrosListados = Persona.objects.all()
    return render(request, "registrosListados.html", {"registros": registrosListados})

def registrarPersona(request):
    dni=request.POST['dni']
    apellido=request.POST['apellido']
    nombre=request.POST['nombre']
    edad=request.POST['edad']

    persona=Persona.objects.create(dni=dni, apellido=apellido, nombre=nombre, edad=edad)

    return redirect('/')

def edicionPersona(request, dni):
    persona=Persona.objects.get(dni=dni)    
    return render(request, "edicionPersona.html", {"persona": persona})

def editarPersona(request):
    dni=request.POST['dni']
    apellido=request.POST['apellido']
    nombre=request.POST['nombre']
    edad=request.POST['edad']

    persona=Persona.objects.get(dni=dni)
    persona.apellido = apellido
    persona.nombre = nombre
    persona.edad = edad

    persona.save()

    return redirect('/')


def eliminarRegistro(request,dni):
    persona=Persona.objects.get(dni=dni)
    persona.delete()

    return redirect('/')