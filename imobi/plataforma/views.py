from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Imovei

@login_required(login_url="/auth/logar") #a pagina só pode ser acessada se o usuario estive logado
def home(request):
  imoveis = Imovei.objects.all
  return render(request, 'home.html', {'imoveis': imoveis})