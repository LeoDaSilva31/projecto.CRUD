from django.shortcuts import render, redirect
from .models import Persona
from django.http import JsonResponse


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

def dnis_registrados(request):
    dnis = Persona.objects.values_list('dni_pasaporte', flat=True)
    return JsonResponse(list(dnis), safe=False)

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

from django.db.models import Q


def buscar_resultados(request):
    query = request.GET.get('q', '')
    campo_busqueda = request.GET.get('campo', 'nombre')
    resultados = None
    search_performed = False

    if query:
        if campo_busqueda == 'nombre':
            resultados = Persona.objects.filter(nombre__icontains=query)
        elif campo_busqueda == 'apellido':
            resultados = Persona.objects.filter(apellido__icontains=query)
        elif campo_busqueda == 'dni_pasaporte':
            resultados = Persona.objects.filter(dni_pasaporte__icontains=query)
        search_performed = True  # Se realizó una búsqueda

    return render(request, 'resultados_busqueda.html', {
        'resultados': resultados,
        'query': query,
        'search_performed': search_performed
    })

