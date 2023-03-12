from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'App_Blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('create_blog/', views.CreateBlog.as_view(), name="create_blog"),
    path('details/<slug>', views.blog_details, name='blog_details'),
]
