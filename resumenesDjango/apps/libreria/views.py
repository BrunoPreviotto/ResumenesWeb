from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from .models import Producto, Categoriaproductos, Subcategoriaproductos, PromocionDescuento

class Inicio(ListView):
    paginate_by = 2
    template_name = 'index.html'
    model = Producto
    context_object_name = 'productos'
    #queryset = Producto.objects.raw('SELECT p.producto, p.descripcion, p.es_stock, p.imagen, pd.nombre, pd.descuento, pd.fecha_caducidad, pd.id_nombre_descuento, nd.nombre, nd.id FROM producto p JOIN libreria_promociondescuento pd ON p.promocion_descuento = pd.id JOIN nombre_descuento nd ON pd.id_nombre_descuento = nd.id')
    queryset = Producto.objects.select_related().filter(es_stock = 1).exclude(promocion_descuento = 1)
    
    

class BarraView(ListView):
    
    template_name = 'barraNavPier.html'
    model= Categoriaproductos
    context_object_name= 'categorias'
    queryset = Categoriaproductos.objects.all()
    
class CategoriasView(ListView):
    template_name = 'categorias.html'
    model= Categoriaproductos
    context_object_name= 'categorias'
    queryset = Categoriaproductos.objects.all()
    
    

    
   
    