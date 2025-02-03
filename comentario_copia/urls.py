from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [    
    path('', views.comentar, name='comentario'),
    path('gravar/', views.gravar, name='gravar'),
    
]
