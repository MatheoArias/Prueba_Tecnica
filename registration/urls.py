from django.urls import path


from .views import SignUpView
from .views import HomePage
from registration.views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', HomePage.as_view(), name="home"),
]
