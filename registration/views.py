from .forms import UserCreationFormWithEmail
from django.views.generic import CreateView
from django import forms
from django.contrib.auth.views import LoginView

# Create your views here.


class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return '?register'

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        form.fields['username'].widget = forms.TextInput(
            attrs={'placeholder': 'Nombre de Usuario'})
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Corre Electrónico'})
        form.fields['password1'].widget = forms.PasswordInput(
            attrs={'placeholder': 'contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(
            attrs={'placeholder': 'Confirme la contraseña'})
        return form


class HomePage(LoginView):
    template_name = 'registration/login.html'
