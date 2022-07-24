from django.contrib import admin
from django.urls import path, include

# El nombre de la aplicación principal será 'register',  con esto en las urls usaré ''register:#nombreapp'
app_name = 'register'

# Incluyo las carpetas de la 'urls' de las aplicaciones
urlpatterns = [


    path('admin/', admin.site.urls),
    path("register/", include("register.urls")),
    path('', include('django.contrib.auth.urls')),
    path('', include('registration.urls')),


]
