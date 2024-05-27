
from django.contrib import admin
from django.urls import path,include
from venta import views

urlpatterns = [
    #path('guerraindex/', admin.site.urls),
    path('index',views.indexprueba),

    #pagina principal y sistema
    path('tecito',views.tecito),
    path('login',views.loginMetodo),
    
    #producto
    path('colleccion',views.producto),
    path('page2',views.producto2),

    #te de verano
    path('teVerano',views.teVerano),

    #te en hoja
    path('teEnHoja',views.teEnHoja),

    #te en bolsa
    path('teNegro',views.teNegro),
    path('teVerde',views.teVerde),

    #bienestar
    path('bPuerh',views.bPuerh),


    #mayorista
    path('mayorista',views.mayorista),

    #blog
    path('blog',views.blog),

    #contacto
    path('contacto',views.contacto),

    #carrito
    path('carrito',views.carrito),

]
