from django import template
from django.shortcuts import render
from django.forms import EmailField
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from bdFamilia.models import BdFamilia
from django.template import Context, Template


'''Una simple bienvenida al desarrollo'''
def bienvenida(request):

    template = loader.get_template('bienvenida.html')
    render = template.render()
    return HttpResponse(render)


'''Función creada para listar a los miembros de la familia ingresados a la bbdd'''
def listar_familia(request):
    miembros = BdFamilia.objects.all
    template = loader.get_template('listaFamilia.html')
    
    familia = BdFamilia.objects.all()

    context_dict = {
        'familia': familia,
    }

    render = template.render(context_dict)
    return HttpResponse(render)


'''Función que permite ingresar miembros de la familia a la bbdd'''
def agregar_miembro(
    request, nombre: str, edad: int, fechaNacimiento: str):
    miembro = BdFamilia(nombre=nombre, edad=edad, fechaNacimiento=fechaNacimiento)
    miembro.save() 
    template = loader.get_template('agregarMiembro.html')
    
    context_dict = {
        'nombre': nombre,
        'edad': edad,
        'fechaNacimiento': fechaNacimiento,
    }
    render = template.render(context_dict)
    return HttpResponse(render)
