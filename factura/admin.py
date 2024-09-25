from django.contrib import admin
from .models import Cliente, Empleado, Categoria, Producto, Factura, DetalleFactura

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre_cliente', 'apellido_cliente', 'RUC', 'direccion')
    search_fields = ('nombre_cliente','apellido_cliente', 'RUC')

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre_empleado', 'apellido_empleado', 'dni_empleado')
    search_fields = ('nombre_empleado', 'apellido_empleado', 'dni_empleado')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre_categoria',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'precio', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('nombre_producto',)

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('numero_factura', 'cliente', 'empleado', 'fecha_factura', 'total')
    list_filter = ('fecha_factura',)
    search_fields = ('numero_factura', 'cliente__nombre_cliente')

@admin.register(DetalleFactura)
class DetalleFacturaAdmin(admin.ModelAdmin):
    list_display = ('factura', 'producto', 'cantidad')  # Se eliminó 'precio' aquí
    search_fields = ('factura__numero_factura', 'producto__nombre_producto')
