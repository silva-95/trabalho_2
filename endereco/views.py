from django.shortcuts import render, redirect
from .models import Endereco
a = {
    'title': 'Endereço'
}
# Create your views here.

def endereco(request):
    return render(request, 'endereco/index.html', a)

def adicionar(request):
    if request.method == "POST":
        novo_registro = Endereco()
        novo_registro.rua = request.POST['rua']
        novo_registro.bairro = request.POST['bairro']
        novo_registro.cidade = request.POST['cidade']
        novo_registro.estado = request.POST['uf']
        novo_registro.pais = request.POST['pais']        
        novo_registro.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))
    return render(request, 'endereco/adicionar.html', a)

