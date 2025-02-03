from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [    
    path('', views.cadastro, name='cadastro'),
    path('gravar/', views.gravar, name='gravar'),
    path('mostrar/', views.mostrar, name='mostrar'),
    path('cadastro/', views.cadastro, name='cadastro'),   
    path('excluir/<int:id>/', views.excluir, name='excluir'),
    path('atualizar/<int:id>/', views.atualizar, name='atualizar'),    
]
