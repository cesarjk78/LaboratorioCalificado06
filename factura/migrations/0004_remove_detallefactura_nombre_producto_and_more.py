# Generated by Django 5.1.1 on 2024-09-24 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0003_alter_factura_igv_alter_factura_subtotal_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallefactura',
            name='nombre_producto',
        ),
        migrations.RemoveField(
            model_name='detallefactura',
            name='precio',
        ),
    ]
