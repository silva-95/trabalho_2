from django.shortcuts import render, redirect
from .models import Pessoa


# Create your views here.
pessoas = Pessoa.objects.all()
contexto = {
    'title': 'Cadastro - CarroShop',
    'pessoas': pessoas
}

def cadastro(request):   
    return render(
                request, 
                "cadastro/index.html",
                contexto
                
                )
# salvar os dados no banco de dados
def gravar(request):
    if request.method == "POST":
        nova_pessoa = Pessoa()
        nova_pessoa.nome=request.POST.get('nome'),
        nova_pessoa.email=request.POST.get('email'),
        nova_pessoa.idade=request.POST.get('idade'),
        nova_pessoa.sexo=request.POST.get('sexo'),
        # nova_pessoa.nascimento=request.POST.get('nascimento'),
        nova_pessoa.telefone=request.POST.get('telefone'),
        
        nova_pessoa.save()
        return redirect('cadastro')  
    return render(request, "cadastro/index.html", contexto)

# mostrar os dados do banco
def mostrar(request):
    pessoas = Pessoa.objects.all()  
    contexto = {
        'title': 'Usuários Cadastrados',
        'pessoas': pessoas
    }
    return render(request, "cadastro/mostrar.html", contexto)

def editar(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    return render(
                request, 
                "cadastro/editar.html",
                {'pessoa': pessoa}
                )

def excluir(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    pessoa.delete()
    return mostrar(request)

def atualizar(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    pessoa.nome = request.POST.get('nome')
    pessoa.email = request.POST.get('email')
    pessoa.idade = request.POST.get('idade')
    pessoa.sexo = request.POST.get('sexo')
    pessoa.nascimento = request.POST.get('nascimento')
    pessoa.telefone = request.POST.get('telefone')
    pessoa.save()
    return mostrar(request)