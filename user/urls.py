from django.contrib import admin
from django.urls import path, include
from user import views

app_name = 'user'

urlpatterns = [
    path('login/', views.login, name='login'), 
    path('cadastro/', views.cadastro, name='cadastro'),
]

