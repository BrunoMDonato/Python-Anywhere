from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, context, loader


# Create your views here.
def Inicio (request):
    return render (request, 'prueba1/index.html')