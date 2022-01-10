from django.shortcuts import render
from django.http import HttpResponse

def cadastro (request):
  #irá retornar uma response = aquilo que é exibido para o usuário
  return HttpResponse('Teste')

def login (request):
  return HttpResponse('Login')

