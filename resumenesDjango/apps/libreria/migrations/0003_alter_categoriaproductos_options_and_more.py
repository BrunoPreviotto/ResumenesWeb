# Generated by Django 4.1.1 on 2022-10-05 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0002_categoriaproductos_subcategoriaproductos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoriaproductos',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='subcategoriaproductos',
            options={'managed': False},
        ),
    ]
