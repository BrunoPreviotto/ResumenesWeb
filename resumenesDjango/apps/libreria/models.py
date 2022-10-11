from tokenize import blank_re
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField, DateTimeField

class Categoriaproductos(models.Model):
    categoria = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'CategoriaProductos'
        
class NombreDescuento(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'nombre_descuento'
        
class PromocionDescuento(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descuento = models.IntegerField(blank=True, null=True)
    fecha_caducidad = models.DateTimeField(blank=True, null=True)
    id_nombre_descuento = models.ForeignKey(NombreDescuento, models.DO_NOTHING, db_column='id_nombre_descuento')
    class Meta:
        managed = False
        db_table = 'libreria_promociondescuento'
    

class Producto(models.Model):
    id = models.IntegerField(primary_key=True)
    producto = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    es_stock = models.CharField(max_length=50, blank=True, null=True)
    imagen = models.CharField(max_length=50, blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)
    categoria = models.ForeignKey(Categoriaproductos, models.DO_NOTHING)
    promocion_descuento = models.ForeignKey(PromocionDescuento, models.DO_NOTHING, db_column='promocion_descuento')
    
    class Meta:
        managed = False
        db_table = 'producto'
        
    def obtener_categoria(self):
        categoria = str([categoria for categoria in self.categoria.all().values_list('categoria', flat=True)]).replace("[", "").replace("]", "").replace("'", "")
        return categoria
    
    def obtenerDescuento(self):
        return self.precio - self.promocion_descuento.descuento
        

    
class Subcategoriaproductos(models.Model):
    subcategoria = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoriaproductos, models.DO_NOTHING, db_column='categoria')

    class Meta:
        managed = False
        db_table = 'SubCategoriaProductos'
       


