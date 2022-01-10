from django.urls import path
from .import views
urlpatterns = {
  # função que recebe  a requisição do usuario e retorna uma response
  path('cadastro/', views.cadastro, name = "cadastro" ),
   path('login/', views.login, name = "login" )
}