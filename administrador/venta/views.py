from django.shortcuts import render


# Create your views here.
def indexprueba(request):
    return render(request,'indexuu.html')

#menu principal
def tecito(request):
    return render(request,'menu/tecito.html')

#login
def loginMetodo(request):
    return render(request,'pagSistema/login.html')


#productos
def producto(request):
    return render(request,'pagProduct/colleccion.html')
def producto2(request):
    return render(request,'pagProduct/page2.html')
    

#te de verano
def teVerano(request):
    return render(request,'pagTeVerano/teVerano.html')

#te en hoja
def teEnHoja(request):
    return render(request,'pagTeEnHoja/teEnHoja.html')

#te en bolsa
def teNegro(request):
    return render(request,'pagTeEnBolsa/teNegro.html')
def teVerde(request):
    return render(request,'pagTeEnBolsa/teVerde.html')

#bienestar
def bPuerh(request):
    return render(request,'pagBienestar/bPuerh.html')



#mayorista
def mayorista(request):
    return render(request,'pagMayorista/mayorista.html')

#blog
def blog(request):
    return render(request,'pagBlog/blog.html')


#contacto
def contacto(request):
    return render(request,'pagContacto/contacto.html')

#carrito
def carrito(request):
    return render(request,'pagCarrito/carrito.html')
