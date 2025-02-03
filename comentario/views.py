from django.shortcuts import render
from .models import Comentario


# Create your views here.


def comentar(request):  
    comentarios = Comentario.objects.all()
    contexto = {
    'title': 'Comentario - CarroShop',
    'comentarios': comentarios
    }
    
    return render(
                request, 
                "comentario/index.html",
                contexto
                
                )
# salvar os dados no banco de dados
def gravar(request):     
    novo_comentario = Comentario()
    novo_comentario.id_comentario = request.POST.get('id_comentario')
    novo_comentario.nome = request.POST.get('nome')
    novo_comentario.descricao = request.POST.get('descricao')
    novo_comentario.save()
    
    return comentar(request)
