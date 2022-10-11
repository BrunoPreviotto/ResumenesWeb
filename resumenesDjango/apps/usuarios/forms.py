from django.contrib.auth.forms import AuthenticationForm

class FormularioLogin(AuthenticationForm):

    def __int__(self, *args, **kargs):
        super(FormularioLogin, self).__init__(*args, **kargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'