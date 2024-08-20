"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import eliminar_categoria, eliminar_marca,marcar_agotado, buscar_productos

urlpatterns = [
    path('index/', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('editar/<str:codigo>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('buscar/', views.buscar_producto, name='buscar_producto'),
    path('agregar_marca/', views.agregar_marca, name='agregar_marca'),
    path('agregar_categoria/', views.agregar_categoria, name='agregar_categoria'),
    path('lista_marcas/', views.lista_marcas, name='lista_marcas'),  # Asegúrate de que esta línea esté presente
    path('lista_categorias/', views.lista_categorias, name='lista_categorias'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('eliminar_categoria/<int:id>/', eliminar_categoria, name='eliminar_categoria'),
    path('eliminar_marca/<int:id>/', eliminar_marca, name='eliminar_marca'),
    path('marcar-agotado/', marcar_agotado, name='marcar_agotado'),
    path('buscar-productos/', buscar_productos, name='buscar_productos'),
    path('marcar-productos_lista/', views.marcar_agotado_lista, name='marcar_agotado_lista'),
    path('buscar-productos_lista/', views.buscar_productos_lista, name='buscar_productos_lista'),
    path('editar_producto/<str:codigo>/', views.editar_producto, name='editar_producto'),
    path('register/', views.register, name='register'),


]
