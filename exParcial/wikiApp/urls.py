from django.urls import path
from . import views

app_name= 'wikiApp' 

urlpatterns = [
    
     #path('',views.hola,name='hola'),
        
    #path('',views.layout,name='layout'),

     path('',views.vistaPrincipal,name='vistaPrincipal'),
           
     path('vistaPrincipal', views.mostrar_temas_y_articulos, name='mostrar_temas_y_articulos'),
     
     path('vistaBusqueda',views.vistaBusqueda,name='vistaBusqueda'),

     #path('vistaPrincipal', views.vistaBusqueda, name='vistaBusqueda'),

     path('vistaCrearNuevotema',views.vistaCrearNuevotema,name='vistaCrearNuevotema'),

     path('vistaCrearNuevoArticulo',views.vistaCrearNuevoArticulo,name='vistaCrearNuevoArticulo'),

     path('vistaArticulos',views.vistaArticulos,name='vistaArticulos'),

 
]