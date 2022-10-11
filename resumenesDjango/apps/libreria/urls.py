from django.urls import path
from .views import CategoriasView, obtenerCategoriasView, BarraView, obtenerSubCategoriasView, obtenerProductosView, obtenerPromoDescuentoView

urlpatterns = [
    path('barra/', BarraView.as_view(), name = 'barra'),
    path('categoriamostrar/', CategoriasView.as_view(), name = 'categoriasmostrar'),
    path('obtenercategorias/', obtenerCategoriasView.as_view(), name = 'obtenercategorias'),
    path('obtenersubcategorias/', obtenerSubCategoriasView.as_view(), name = 'obtenersubcategorias'),
    path('obtenerproducto/', obtenerProductosView.as_view(), name = 'obtenerproducto'),
    path('obtenerpromodescuento/', obtenerPromoDescuentoView.as_view(), name = 'obtenerpromodescuento'),
]