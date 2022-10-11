from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Resumen







class ListadoResumenes(ListView):
    model = Resumen
    template_name = 'listadoResumenes.html'
    context_object_name = 'resumenes'
    queryset = Resumen.objects.filter(id = 1)

