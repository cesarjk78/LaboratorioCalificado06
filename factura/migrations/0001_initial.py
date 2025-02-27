# Generated by Django 5.1.1 on 2024-09-24 01:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(max_length=255)),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
                ('RUC', models.CharField(max_length=11, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('codigo_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_empleado', models.CharField(max_length=255)),
                ('apellido_empleado', models.CharField(max_length=255)),
                ('dni_empleado', models.CharField(max_length=8, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('numero_factura', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_factura', models.DateField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('igv', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factura.cliente')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factura.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=255)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factura.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=255)),
                ('cantidad', models.PositiveIntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factura.factura')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factura.producto')),
            ],
        ),
    ]
