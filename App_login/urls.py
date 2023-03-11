from django.urls import path
from . import views

app_name = "App_login"

urlpatterns = [
    path("signup/", views.sign_up, name="signup"),
]
