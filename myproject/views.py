from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Categoria
from .models import Marca
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

def index(request):
    return HttpResponse("<h1>Hola mundo</h1>")

from django.shortcuts import render, redirect
from .models import Producto, Categoria, Marca

@login_required
def agregar_producto(request):

    if request.method == "POST":
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        stock = request.POST['stock']
        categoria_id = request.POST['categoria']
        marca_id = request.POST['marca']
        codigo = request.POST['codigo']
        
        # Obtener instancias de categoria y marca
        categoria = Categoria.objects.get(id=categoria_id)
        marca = Marca.objects.get(id=marca_id)
        
        nuevo_producto = Producto(
            nombre=nombre, 
            precio=precio, 
            stock=stock, 
            categoria=categoria, 
            codigo=codigo, 
            marca=marca
        )
        nuevo_producto.save()
        return redirect('agregar_producto')
    
    # Obtener todas las categorías y marcas
    categorias = Categoria.objects.all()
    marcas = Marca.objects.all()
    productos = Producto.objects.all()
    
    context = {
        'categorias': categorias,
        'marcas': marcas,
        'productos': productos,  # Pasar los productos al contexto
    }
    
    return render(request, 'agregar_producto.html', context)

@login_required
def eliminar_categoria(request, id):
    if request.method == "POST":
        categoria = get_object_or_404(Categoria, id=id)
        categoria.delete()
    return redirect('agregar_categoria')


def eliminar_marca(request, id):
    if request.method == 'POST':
        marca = get_object_or_404(Marca, id=id)
        marca.delete()
        return redirect('agregar_marca')  # Redirige a la página de agregar marcas
    else:
        return HttpResponse("Método no permitido", status=405)
    
@login_required
def lista_marcas(request):
    marcas = Marca.objects.all()
    return render(request, 'listar_marcas.html', {'marcas': marcas})

@login_required
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'marcas': productos})

@login_required
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'lista_categorias.html', {'categorias': categorias})

@login_required
def agregar_marca(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        nueva_marca = Marca(nombre=nombre)
        nueva_marca.save()
        return redirect('agregar_marca')
    marcas = Marca.objects.all()
    return render(request, 'agregar_marca.html', {'marcas': marcas})

@login_required
def agregar_categoria(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        nueva_categoria = Categoria(nombre=nombre)
        nueva_categoria.save()
        return redirect('agregar_categoria')  # Redirige a la lista de categorías o donde prefieras
    categorias = Categoria.objects.all()
    return render(request, 'agregar_categoria.html', {'categorias': categorias})

@login_required
def editar_producto(request, codigo):
    producto = get_object_or_404(Producto, codigo=codigo)
    categorias = Categoria.objects.all()
    marcas = Marca.objects.all()

    if request.method == "POST":
        producto.nombre = request.POST['nombre']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.categoria = Categoria.objects.get(id=request.POST['categoria'])
        producto.marca = Marca.objects.get(id=request.POST['marca'])
        producto.save()
        return redirect('lista_productos')

    return render(request, 'editar_producto.html', {
        'producto': producto,
        'categorias': categorias,
        'marcas': marcas,
    })

@login_required
def eliminar_producto(request, id):
    if request.method == 'POST':
        producto = get_object_or_404(Producto, id=id)
        producto.delete()
        return redirect('agregar_producto')  # Redirige a la página de agregar productos
    else:
        return HttpResponse("Método no permitido", status=405)
@login_required
def lista_productos(request):
    categorias = Categoria.objects.all()
    marcas = Marca.objects.all()
    productos = Producto.objects.all()
    
    context = {
        'categorias': categorias,
        'marcas': marcas,
        'productos': productos,  # Pasar los productos al contexto
    }    
    return render(request, 'lista_productos.html', context)

@login_required
def buscar_producto(request):
    if request.method == "GET":
        query = request.GET.get('query')
        resultados = Producto.objects.filter(nombre__icontains=query)
        return render(request, 'buscar_producto.html', {'resultados': resultados})
    return render(request, 'buscar_producto.html')

# def marcar_agotado(request, codigo):
#     producto = get_object_or_404(Producto, codigo=codigo)
#     producto.stock = 0
#     producto.save()
#     return redirect('detalle_producto', codigo=producto.codigo)
@login_required
def marcar_agotado(request):
    productos_ids = [key.split('_')[1] for key in request.POST.keys() if key.startswith('agotado_')]
    Producto.objects.filter(id__in=productos_ids).update(stock=0)
    return redirect('agregar_producto')

@login_required
def marcar_agotado_lista(request):
    productos_ids = [key.split('_')[1] for key in request.POST.keys() if key.startswith('agotado_')]
    Producto.objects.filter(id__in=productos_ids).update(stock=0)
    return redirect('lista_productos')

@login_required
def buscar_productos(request):
    query = request.GET.get('q', '')
    if query:
        productos = Producto.objects.filter(nombre__icontains=query)
    else:
        productos = Producto.objects.all()
    return render(request, 'agregar_producto.html', {'productos': productos})

@login_required
def buscar_productos_lista(request):
    query = request.GET.get('q', '')
    if query:
        productos = Producto.objects.filter(nombre__icontains=query)
    else:
        productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')  # Redirige a la página de inicio u otra página
        else:
            # Manejar el caso en el que las credenciales son incorrectas
            return render(request, 'login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')  # Redirige a la página de login

def user_profile(request):
    return render(request, 'profile.html', {'user': request.user})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')  # Redirige a la página principal o al dashboard
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})

@login_required
def index(request):
    return render(request, 'index.html')
