from django.urls import path
from . import views

app_name = "App_login"

urlpatterns = [
    path("signup/", views.sign_up, name="register"),
    path('login/', views.sign_in, name="login"),
    path('logout/', views.sign_out, name="logout"),
]
