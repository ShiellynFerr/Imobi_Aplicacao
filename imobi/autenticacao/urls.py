from django.urls import path
from .import views
urlpatterns = [
  # função que recebe  a requisição do usuario e retorna uma response
  path('cadastro/', views.cadastro, name = "cadastro" ),
  path('logar/', views.logar , name = "logar" ),
   path('logar/', views.sair , name = "logar" ),
]