from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=100, unique=True)  # Campo único

    def __str__(self):
        return self.nombre

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
        self.save()

    def actualizar_stock(self, nueva_cantidad):
        self.stock = nueva_cantidad
        self.save()

    def marcar_como_agotado(self):
        self.stock = 0
        self.save()

    def obtener_informacion(self):
        return f"{self.nombre} - {self.marca} - {self.categoria}: ${self.precio}"

class Usuario(models.Model):
    ROLES = (
        ('Admin', 'Admin'),
        ('Empleado', 'Empleado'),
    )
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    rol = models.CharField(max_length=10, choices=ROLES)
    password = models.CharField(max_length=255)

    def login(self, email, password):
        # Implementación del login
        pass

    def logout(self):
        # Implementación del logout
        pass

    def cambiar_password(self, nuevo_password):
        self.password = nuevo_password
        self.save()

class Admin(Usuario):
    def agregar_producto(self, producto):
        # Implementación para agregar producto
        pass

    def editar_producto(self, producto):
        # Implementación para editar producto
        pass

    def eliminar_producto(self, codigo):
        # Implementación para eliminar producto
        pass

    def generar_reporte_productos_agotados(self):
        # Implementación para generar reporte de productos agotados
        pass

class Empleado(Usuario):
    def buscar_producto(self, nombre):
        # Implementación para buscar producto
        pass

    def marcar_producto_agotado(self, producto):
        # Implementación para marcar producto como agotado
        pass

class Inventario(models.Model):
    productos = models.ManyToManyField(Producto)

    def agregar_producto(self, producto):
        self.productos.add(producto)

    def eliminar_producto(self, codigo):
        producto = Producto.objects.get(codigo=codigo)
        self.productos.remove(producto)

    def buscar_producto(self, nombre):
        return self.productos.filter(nombre__icontains=nombre)

    def actualizar_producto(self, codigo, producto):
        prod = self.productos.get(codigo=codigo)
        prod.nombre = producto.nombre
        prod.precio = producto.precio
        prod.stock = producto.stock
        prod.categoria = producto.categoria
        prod.marca = producto.marca
        prod.save()