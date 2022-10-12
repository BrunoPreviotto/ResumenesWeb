from cProfile import label
from dataclasses import field
from pickle import TRUE
from tkinter import Widget
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from tkinter import Widget

class RegistroForm(UserCreationForm):
    
    class Meta:
        model= User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels={
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo',
        }

class LoginForm(AuthenticationForm):
    class Meta:
        model= User
        fields= ['username', 'password', 'remember_me']
        #username = forms.CharField(max_length= 100, required=True, Widget=forms.TextInput(attrs={'placeholder': 'Usuario', 'class': 'bg-danger'}))
        #password = forms.CharField(max_length= 100, required=True, Widget=forms.TextInput(attrs={'placeholder': 'Contraseña', 'id': 'contraseña'})) 
        remember_me = forms.BooleanField(required=False)