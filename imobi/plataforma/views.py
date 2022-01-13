from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
def home(request):
  return HttpResponse('Estou na Home')
