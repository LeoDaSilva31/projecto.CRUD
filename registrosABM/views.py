from django.shortcuts import render, redirect
from .models import Persona


# Create your views here.
def home(request):
    registrosListados = Persona.objects.all()
    return render(request, "registrosListados.html", {"registros": registrosListados})

def registrarPersona(request):
    dni_pasaporte=request.POST['dni_pasaporte']
    apellido=request.POST['apellido']
    nombre=request.POST['nombre']
    fecha_entrada=request.POST['fecha_entrada']
    fecha_salida=request.POST['fecha_salida']
    numero_habitacion=request.POST['numero_habitacion']
   

    persona=Persona.objects.create(dni_pasaporte=dni_pasaporte, apellido=apellido, nombre=nombre, fecha_entrada=fecha_entrada, fecha_salida=fecha_salida, numero_habitacion=numero_habitacion)

    return redirect('/')

def edicionPersona(request, dni_pasaporte):
    persona=Persona.objects.get(dni_pasaporte=dni_pasaporte)    
    return render(request, "edicionPersona.html", {"persona": persona})

def editarPersona(request):
    dni_pasaporte=request.POST['dni_pasaporte']
    apellido=request.POST['apellido']
    nombre=request.POST['nombre']
    #fecha_entrada=request.POST['fecha_entrada']
    fecha_salida=request.POST['fecha_salida']
    numero_habitacion=request.POST['numero_habitacion']

    persona=Persona.objects.get(dni_pasaporte=dni_pasaporte)
    persona.apellido = apellido
    persona.nombre = nombre
    #persona.fecha_entrada=fecha_entrada
    persona.fecha_salida=fecha_salida
    persona.numero_habitacion=numero_habitacion

    persona.save()

    return redirect('/')


def eliminarRegistro(request,dni_pasaporte):
    persona=Persona.objects.get(dni_pasaporte=dni_pasaporte)
    persona.delete()

    return redirect('/')

