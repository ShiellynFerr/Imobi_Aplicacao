from http.client import HTTPResponse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('imovel/<str:id>', views.imovel, name="imovel"),
]

