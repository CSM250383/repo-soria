from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse

listaTemas = [
    ['Frameworks','Django y Flask son los principales frameworks para crear aplicaciones web con Python de forma rápida y eficiente'],
    ['Backend','Python se usa para construir la lógica del servidor, interactuando con bases de datos y creando APIs.'],
    ['Bases de Datos','Python se conecta a diferentes tipos de bases de datos (SQL y NoSQL) para almacenar y gestionar información.']
]

listaArticulos = [
    ['Artículo 1.1','Frameworks','Contenido del Artículo 1.1'],    
    ['Artículo 1.2','Frameworks','Contenido del Artículo 1.2'],    
    ['Artículo 2.1','Backend','Contenido del Artículo 2.1'],    
    ['Artículo 3.1','Bases de Datos','Contenido del Artículo 3.1'],   
    ['Artículo 3.2','Bases de Datos','Contenido del Artículo 3.2']   
]


# Create your views here.
def hola(request):
    return HttpResponse("Bienvenidos a mi Web- Gestión de Temas y Artículos")

def layout(request):
    return render (request,'layout.html', {
        'listaTemas':listaTemas,
        'listaArticulos':listaArticulos, 
    })

def vistaPrincipal(request):
    return render (request,'vistaPrincipal.html',{
        'listaTemas': listaTemas,
        'listaArticulos':listaArticulos, 
    })

def vistaCrearNuevotema(request):
    if request.method =='POST':
        nombreTema = request.POST.get('nombreTema')
        descripcionTema = request.POST.get('descripcionTema')
        
        print(request.POST)

        print(nombreTema)
        print(descripcionTema)

        listaTemas.append([nombreTema,descripcionTema])

        # return HttpResponseRedirect(reverse('wikiApp:vistaPrincipal'))
    return render (request,'vistaCrearNuevoTema.html', {
        'listaTemas':listaTemas,
         'listaArticulos':listaArticulos,
    })

def vistaCrearNuevoArticulo(request):
        
        tituloArticulo = None
        temaSeleccionado = None
        contenidoArticulo = None

        if request.method =='POST':

            tituloArticulo  = request.POST.get('tituloArticulo')
            temaSeleccionado = request.POST.get('temaSeleccionado')
            contenidoArticulo = request.POST.get('contenidoArticulo')
            
            print (request.POST)

            listaArticulos.append([tituloArticulo,temaSeleccionado,contenidoArticulo])
            
           # return HttpResponseRedirect(reverse('wikiApp:vistaArticulos'))

            return render (request,'vistaArticulos.html', {
            'listaArticulos':listaArticulos, 
            'listaTemas':listaTemas
            })
        return render (request,'vistaCrearNuevoArticulo.html', {
            'listaTemas':listaTemas
        })

def mostrar_temas_y_articulos(request):
        # Obtener el tema seleccionado desde los parámetros GET
        tema_seleccionado = request.GET.get('tema','Frameworks')
        
        # Filtrar los artículos según el tema seleccionado
        if tema_seleccionado:
            articulos_filtrados = [articulo for articulo in listaArticulos if articulo[1] == tema_seleccionado]
        else:
            articulos_filtrados = []

        context = {
            'listaTemas': listaTemas,
            'listaArticulos': articulos_filtrados,
            'tema_seleccionado': tema_seleccionado,
        }

        # Pasar las listas a la plantilla
        return render(request, 'vistaPrincipal.html', context)

def vistaArticulos(request):
    return render (request,'vistaArticulos.html', {
         'listaTemas': listaTemas,
         'listaArticulos':listaArticulos,
    })

def vistaBusqueda(request):

    # Obtiene el término de búsqueda desde el formulario GET
    query = request.GET.get('q', '')
    resultados = []

    if query:
    # Filtra los artículos que contienen el término de búsqueda en cualquier campo
     resultados = [art for art in listaArticulos if query.lower() in art[0].lower() or query.lower() in art[1].lower() or query.lower() in art[2].lower()]

    return render (request, 'vistaBusqueda.html', {
        'resultados': resultados,
        'query': query,
        'listaTemas':listaTemas,
    })
