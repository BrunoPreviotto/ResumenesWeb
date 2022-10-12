from operator import imod
from tempfile import template
from django.shortcuts import redirect
from django.urls import path
from .views import RegistrarUsuario, LoginUsuario
from .forms import LoginForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registrar/', RegistrarUsuario.as_view(), name = 'registrar'),
    path('login/', LoginUsuario.as_view(redirect_authenticated_user=True, template_name='usuario/login.html', authentication_form=LoginForm), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuario/logout.html'), name = 'logout'),
]

