from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def saludo(request):
    fecha_hora = datetime.now()
    return HttpResponse("Hola mundo "+str(fecha_hora))

def saludar_a(request, nombre):
    return HttpResponse("Hola, como estas "+nombre.capitalize())
