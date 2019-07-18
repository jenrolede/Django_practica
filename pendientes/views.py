from django.shortcuts import render
from django.http import HttpResponse

from pendientes.models import Tarea# importamos la clase tarea de models 
from random import randint
# Create your views here.

def index(request): 
    listita = Tarea.objects.all() #consultamos la BDy guardamos todos
                                # los registros de la tabla Tarea
                                # como objetos y guardamos en listita
    persona = {
        "nombre":"Jenny",
        "Edad":20,
        "Hobbies":["Bailar", "Dibujar", "Cantar"],
        "lista_tareas": listita, # agregamos la clave lista_tareas
                                 # al diccionario de contenido con la
                                 #
    }
    return render(request, "inicio.html", persona)

def tarea(request):
    return HttpResponse("hola soy la vista de tarea")

def respuesta(request):
    return HttpResponse("hola soy la vista de respuesta")

#def aleatorio(request):
    #numero =str(randint(500,999))
