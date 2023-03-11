from django.urls import path
from . import views


app_name = "App_login"

urlpatterns = [
    path("signup/", views.sign_up, name="register"),
    path('login/', views.sign_in, name="login"),
    path('logout/', views.sign_out, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('change_profile/', views.change_profile, name="change_profile"),
    path('password/', views.change_pass, name="change_pass"),
    path('profile_pic/', views.add_pro_pic, name="add_pro_pic"),
    path('change_picture/', views.change_pro_pic, name='change_pro_pic')
]
