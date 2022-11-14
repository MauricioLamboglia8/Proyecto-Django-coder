from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader 
from appcoder.models import *
from appcoder.forms import *



# Create your views here.
def inicio(request):
    return render(request, 'appcoder/inicio.html')

def cursos(request):
    
    return render(request, 'appcoder/cursos.html')


def creacion_curso(request):
    
    if request.method == 'POST':
       
        nombre_curso = request.POST['curso']
        numero_camada = request.POST['camada']
        curso = Curso(nombre=nombre_curso, camada=numero_camada)
        curso.save()
    
    return render(request, 'appcoder/curso_formulario.html')

def buscar_curso(request):
    return render(request, 'appcoder/busqueda_cursos.html')

def resultado_busqueda_cursos(request):
    
    nombre_curso = request.GET["nombre_curso"]
    curso = Curso.objects.filter(nombre__icontains=nombre_curso)
    contexto = {'curso': curso}
   
    return render(request, 'appcoder/resultados_busqueda_cursos.html', contexto)



def estudiantes(request):
    return render(request, 'appcoder/estudiantes.html')


def profesores(request):
    return render(request, 'appcoder/profesores.html')


def creacion_profesores(request):

    if request.method == 'POST':
        formulario = ProfesorFormulario(request.POST)
       
        if formulario.is_valid():
           
            data = formulario.cleaned_data

        profesor = Profesor(nombre=data['nombre'], apellido=data['apellido'], email=data['email'], profesion=data['profesion'])

        profesor.save()
    

    formulario = ProfesorFormulario()
    
    contexto = {'formulario': formulario}

    return render(request, 'appcoder/profesores_formulario.html', contexto)



def entregables(request):
    return render(request, 'appcoder/entregables.html')

