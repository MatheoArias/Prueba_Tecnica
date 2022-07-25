from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormUser(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',           
        ]
        labels={
            'last_login':'última conexión',
            'username':'Nombre de Usuario',
            'first_name':'Primer Nombre',
            'last_name':'Apellidos',
            'email':'Correo Electrónico',
        }
        
