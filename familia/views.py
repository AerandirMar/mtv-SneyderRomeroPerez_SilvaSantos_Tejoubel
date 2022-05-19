from django.forms import EmailField
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context
from datetime import datetime
from django.template import loader
from bdFamilia.models import BdFamilia


def bienvenida(request):

    template = loader.get_template('bienvenida.html')
    render = template.render()
    return HttpResponse(render)


def listar_familia(request):
    miembros = BdFamilia.objects.all
    template = loader.get_template('listaFamilia.html')
    
    familia = BdFamilia.objects.all()

    context_dict = {
        'familia': familia,
    }

    render = template.render(context_dict)
    return HttpResponse(render)

