# Generated by Django 4.1.1 on 2022-10-05 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0003_alter_categoriaproductos_options_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='categoriaproductos',
            table='CategoriaProductos',
        ),
        migrations.AlterModelTable(
            name='subcategoriaproductos',
            table='SubCategoriaProductos',
        ),
    ]