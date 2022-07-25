from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .forms import FormUser

class Signup(CreateView):
    model=User
    template_name = 'registration/signup.html'
    form_class=FormUser

    def get_success_url(self):
        return '?register'


class HomePage(LoginView):
    template_name = 'registration/login.html'
