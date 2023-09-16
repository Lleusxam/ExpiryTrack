from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('listagem', views.listagem, name='listagem'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]
