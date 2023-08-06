from django.contrib import admin
from django.urls import path, include
from user import views

app_name = 'user'

urlpatterns = [
    path('', views.home, name=''),
    path('login/', views.login_user, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('plataforma/', views.plataforma, name='plataforma'),
]

