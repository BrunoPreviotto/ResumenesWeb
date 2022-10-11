from django.urls import path
from django.views.generic import TemplateView
from .views import ListadoResumenes


urlpatterns = [
    path('listar_resumenes/', ListadoResumenes.as_view(), name = 'listar_resumenes'),
]
