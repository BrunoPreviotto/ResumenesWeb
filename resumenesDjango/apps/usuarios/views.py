from ast import If
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import RegistroForm, LoginForm
from django.contrib import messages
from django.views import View

class RegistrarUsuario(View):
    template_name= "usuario/registrar.html"
    initial= {'key': 'value'}
    form_class= RegistroForm
    
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect(to='/')
        return render(request, self.template_name, {'form': form})
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='/')
        return super(RegistrarUsuario, self).dispatch(request, *args, **kwargs)

class LoginUsuario(LoginView):
    form_class= LoginForm
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super(LoginUsuario, self).form_valid(form)
