from django.urls import path
from . import views

urlpatterns = [
    path("sign-up/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
]
