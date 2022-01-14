from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Imovei, Cidade
from django.shortcuts import get_object_or_404

@login_required(login_url="/auth/logar") #a pagina só pode ser acessada se o usuario estive logado
def home(request):
  preco_minimo = request.GET.get('preco_minimo')
  preco_maximo = request.GET.get('preco_maximo')
  cidade = request.GET.get('cidade')
  tipo = request.GET.getlist('tipo')
  if preco_minimo or preco_maximo or cidade or tipo:

#Verificação do filtro
    if not preco_minimo:
       preco_minimo = 0
    if not preco_maximo:
         preco_maximo = 999999999999
    if not tipo:
         tipo = ['A', 'C']

   
    imoveis = Imovei.objects.filter(valor__gte=preco_minimo).filter(valor__lte=preco_maximo).filter(tipo_imovel__in=tipo).filter(cidade=cidade)
  else:
    imoveis = Imovei.objects.all()

  cidades = Cidade.objects.all
  return render(request, 'home.html', {'imoveis': imoveis, 'cidades': cidades})

def imovel(request, id):
    imovel = get_object_or_404(Imovei, id=id)
    sugestoes = Imovei.objects.filter(cidade=imovel.cidade).exclude(id=id)[:2]
    print(imovel)
    return render(request, 'imovel.html', {'imovel': imovel, 'sugestoes': sugestoes , 'id': id})
