from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.endereco, name='endereco'),
    path('adicionar/', views.adicionar, name='adicionar'),
]