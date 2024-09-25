from django.db import models
from decimal import Decimal
from django.db.models.signals import post_save
from django.dispatch import receiver

class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=255)
    apellido_cliente = models.CharField(max_length=100, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True)
    RUC = models.CharField(max_length=11, unique=True)
    
    
    def __str__(self):
        return f"{self.nombre_cliente} {self.apellido_cliente}"

class Empleado(models.Model):
    codigo_empleado = models.AutoField(primary_key=True)
    nombre_empleado = models.CharField(max_length=255)
    apellido_empleado = models.CharField(max_length=255)
    dni_empleado = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return f'{self.nombre_empleado} {self.apellido_empleado}'

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_categoria

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_producto

class Factura(models.Model):
    numero_factura = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha_factura = models.DateField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    igv = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def update_totals(self):
        # Calcula el subtotal, IGV y total
        self.subtotal = sum(detalle.valor_venta for detalle in self.detallefactura_set.all())
        self.igv = self.subtotal * Decimal('0.18')
        self.total = self.subtotal + self.igv
        self.save()  # Guarda los cambios
    def __str__(self):
        return f'Factura {self.numero_factura}'

@receiver(post_save, sender=Factura)
def calculate_totals(sender, instance, created, **kwargs):
    if created:  # Solo actualiza los totales si la factura es creada
        instance.update_totals()

class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    @property
    def valor_venta(self):
        return self.cantidad * self.producto.precio  # Calcula el valor de venta

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.factura.save()  # Esto recalcula subtotal, IGV y total
