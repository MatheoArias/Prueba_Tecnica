from django.contrib import admin
from django.urls import path,include

app_name='register'
urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", include("register.urls"))
]
