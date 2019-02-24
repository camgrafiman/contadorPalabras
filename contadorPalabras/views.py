from django.http import HttpResponse
from django.shortcuts import render
import operator
#redirige a home.html dentro de templates:
def home(request):
    return render(request, 'home.html', {'variableApasar': 'Mi primera página con Django y Python!!'})

def contacto(request):
    return HttpResponse('Página de contacto')

def blog(request):
    return HttpResponse('<h2>BLOG</h2>')

def aboutme(request):
    return render(request, 'aboutme.html')

def acerca(request):
    nombre1 = request.GET.get('nombre')
    apellidos1 = request.GET.get('apellidos')
    edad1 = request.GET.get('edad')
    profesion1 = request.GET.get('profesion')
    return render(request, 'acerca.html', {'nombre': nombre1, 'apellidos': apellidos1, 'edad': edad1, 'profesion': profesion1})

def contador(request):
    #area1 = request.GET['area1']
    area1 = request.GET.get('area1')
    palabras = area1.split() 

    dictPalabras = dict()

    for palabra in palabras:
        if palabra in dictPalabras:
            #incrementar:
            dictPalabras[palabra] +=1
        else:
            #agregar al diccionario:
            dictPalabras[palabra] = 1

    ordenPalabras = sorted(dictPalabras.items(), key=operator.itemgetter(1), reverse=True )

    return render(request, 'contador.html', {'area1': area1, 'contar':len(palabras),  'ordenPalabras':ordenPalabras})