from django.db import models
from datetime import timedelta

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    apellidos = models.CharField(max_length=220, blank=False, null=False)
    estado = models.BooleanField('Estado', default=True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']

    def natural_key(self):
        return f'{self.nombre} {self.apellidos}'

    def __str__(self):
        return self.nombre

class Resumen(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Título', max_length=255, blank=False, null=False)
    fecha_publicacion = models.DateField('Fecha de publicación', blank=False, null=False)
    descripcion = models.TextField('Descripción', null=True, blank=True)
    imagen = models.ImageField('Imagen', max_length=255, null=True, blank=True)
    autor = models.ManyToManyField(Autor)
    fecha_creacion = models.DateField('Fecha de creación', auto_now=True, auto_now_add=False)
    estado = models.BooleanField(default=True, verbose_name='Estado')

    def natural_key(self):
        return self.titulo

    class Meta:
        verbose_name = 'Resumen'
        verbose_name_plural = 'Resumenes'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo

    def obtener_autores(self):
        nombre = str([autor for autor in self.autor.all().values_list('nombre', flat=True)]).replace("[", "").replace("]", "").replace("'", "")
        apellido = str([autor for autor in self.autor.all().values_list('apellidos', flat=True)]).replace("[", "").replace("]", "").replace("'", "")
        autores = nombre +  " " + apellido
        return autores

