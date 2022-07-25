from django.urls import path
from .views import HomePage, Signup


urlpatterns = [
    path('signup/', Signup.as_view(), name='signup'),
    path('', HomePage.as_view(), name="home"),
]
