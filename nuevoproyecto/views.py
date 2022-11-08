from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader




def vista_saludo(request):
    return HttpResponse('Hola Mundo')


def iniciar_sesion(request):
    return HttpResponse('Pasame usuario y password')


def dia_hoy(request, nombre):
    hoy = datetime.now()
    repuesta = f'Hoy es {hoy}- Bienvenido {nombre}'
    return HttpResponse(repuesta)

def nacimiento(request, edad):
    edad = int(edad)
    anio_edad = datetime.now().year - edad 
    return HttpResponse(f'vos naciste en {anio_edad}')



def vista_plantilla(request):
   
    plantilla = loader.get_template('plantilla_bonita.html')
    
    datos = {'nombre': 'Mauricio', 'fecha': datetime.now(), 'apellido': 'Lamboglia', 'edad': [24, 34, 35, 36]}

    documento = plantilla.render(datos)
   
    return HttpResponse(documento)



def vista_listado_alumnos(request):

    archivo = open(r'C:\Users\anala\OneDrive\Desktop\Entregas Curso\VS Python\nuevoproyecto\nuevoproyecto\nuevoproyecto\templates\listado_alumnos.html')
    
    plantilla = Template(archivo.read())
    
    archivo.close()

    listado_alumnos = ['Lionel Gareis', 'Agustin Russo', 'Cristian Garcia', 'Angel Pettinari', 'Diego Ibarra', 'Santiago Ortiz', 'Mauricio Lamboglia', 'Barbara Vivante', 'Barbara Pino']

    datos = {'tecnologia': 'Python', 'listado_alumnos': listado_alumnos}

    Contexto = Context(datos)

    documento = plantilla.render(Contexto)
    return HttpResponse(documento)


def vista_listado_alumnos2(request):
    listado_alumnos = ['Lionel Gareis', 'Agustin Russo', 'Cristian Garcia', 'Angel Pettinari', 'Diego Ibarra', 'Santiago Ortiz', 'Mauricio Lamboglia', 'Barbara Vivante', 'Barbara Pino']

    datos = {'tecnologia': 'Python', 'listado_alumnos': listado_alumnos}
    
    plantilla = loader.get_template('listado_alumnos.html')
    documento = plantilla.render(datos)
    
    return HttpResponse(documento)



