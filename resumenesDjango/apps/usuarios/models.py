from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Usuario(models.Model):
    username = models.CharField('Nombre de usuario', unique=True, max_length=100)
    email = models.EmailField('Correo Electrónico', max_length=254, unique=True)
    nombres = models.CharField('Nombres', max_length=200, blank=True, null=True)
    apellidos = models.CharField('Apellidos', max_length=200, blank=True, null=True)

    imagen = models.ImageField('Imagen de Perfil', upload_to='perfil/', max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombres', 'apellidos']

    def __str__(self):
        return f'{self.nombres},{self.apellidos}'

    def has_perm(self, per, obj = None):
        return True

    def has_moudule_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_staff



