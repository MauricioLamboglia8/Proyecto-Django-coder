from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader


def inicio(request):
    return HttpResponse('Estas en el inicio')

def cursos(request):
    return HttpResponse('Estas en cursos')

def estudiantes(request):
    return HttpResponse('Estas en estudiantes')

def profesores(request):
    return HttpResponse('Estas en profesores')

def entregables(request):
    return HttpResponse('Estas en entregables')