from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [    
    path('', views.comentar, name='comentario'),
    path('armazenar/', views.armazenar, name='armazenar'),
    
]
