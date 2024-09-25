from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Factura
from decimal import Decimal

class FacturaListView(ListView):
    model = Factura
    template_name = 'factura/facturas_list.html'
    context_object_name = 'facturas'

class FacturaDetailView(DetailView):
    model = Factura
    template_name = 'factura/factura_detail.html'
    context_object_name = 'factura'  # Añadir el nombre de contexto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        factura = self.object

        detalles = []
        subtotal = Decimal('0.00')  # Inicializa el subtotal

        for detalle in factura.detallefactura_set.all():
            valor_venta = detalle.cantidad * detalle.producto.precio  # Calcular valor de venta
            subtotal += valor_venta  # Sumar al subtotal
            detalles.append({
                'producto': detalle.producto.nombre_producto,  # Descripción del producto
                'cantidad': detalle.cantidad,
                'precio_unitario': detalle.producto.precio,  # Precio unitario del producto
                'valor_venta': valor_venta,  # Valor de venta calculado
            })

        igv = subtotal * Decimal('0.18')  # Calcular IGV (18%)
        total = subtotal + igv  # Calcular el total

        # Agregar información al contexto
        context['detalles'] = detalles
        context['subtotal'] = subtotal
        context['igv'] = igv
        context['total'] = total
        context['ruc'] = factura.cliente.RUC  
        context['empleado'] = factura.empleado.nombre_empleado  
        return context
