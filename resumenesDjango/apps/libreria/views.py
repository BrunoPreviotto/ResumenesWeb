import json
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F
from django.core.paginator import Paginator
from .models import Producto, Categoriaproductos, Subcategoriaproductos, PromocionDescuento

class Inicio(ListView):
    paginate_by = 5
    template_name = 'index.html'
    model = Producto
    context_object_name = 'productos'
    #queryset = Producto.objects.raw('SELECT p.producto, p.descripcion, p.es_stock, p.imagen, pd.nombre, pd.descuento, pd.fecha_caducidad, pd.id_nombre_descuento, nd.nombre, nd.id FROM producto p JOIN libreria_promociondescuento pd ON p.promocion_descuento = pd.id JOIN nombre_descuento nd ON pd.id_nombre_descuento = nd.id')
    queryset = Producto.objects.select_related().filter(promocion_descuento = 4)
    
    

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
    
    
class obtenerCategoriasView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            categorias=list(Categoriaproductos.objects.all().values())
            if len(categorias) > 0:
                cat = categorias[0]
                datos = {'message': "Success", 'categoria': cat}
            return JsonResponse(datos)
        else:
            categorias = list(Categoriaproductos.objects.values())
            if len(categorias)>0:
                datos={'message':"Success", 'categorias':categorias}
            return JsonResponse(datos)
        
class obtenerSubCategoriasView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            categorias=list(Subcategoriaproductos.objects.all().values())
            if len(categorias) > 0:
                cat = categorias[0]
                datos = {'message': "Success", 'subcategoriacategoria': cat}
            return JsonResponse(datos)
        else:
            categorias = list(Subcategoriaproductos.objects.values())
            if len(categorias)>0:
                datos={'message':"Success", 'categorias':categorias}
            return JsonResponse(datos)
        
class obtenerProductosView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            producto=list(Producto.objects.all().values())
            if len(producto) > 0:
                cat = producto[0]
                datos = {'message': "Success", 'subcategoriacategoria': cat}
            return JsonResponse(datos)
        else:
            producto = list(Producto.objects.values())
            if len(producto)>0:
                datos={'message':"Success", 'producto':producto}
            return JsonResponse(datos)
        
class obtenerPromoDescuentoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id > 0):
            promodescuento=list(PromocionDescuento.objects.all().values())
            if len(promodescuento) > 0:
                cat = promodescuento[0]
                datos = {'message': "Success", 'subcategoriacategoria': cat}
            return JsonResponse(datos)
        else:
            promodescuento = list(PromocionDescuento.objects.values())
            if len(promodescuento)>0:
                datos={'message':"Success", 'promodescuento':promodescuento}
            return JsonResponse(datos)
    
   
    