from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User # importando tabela usuario


 #irá retornar uma response = aquilo que é exibido para o usuário
def cadastro (request):
  if request.method == "GET" :
   return render(request, 'cadastro.html')
  elif request.method == "Post":
   username = request.Post.get("username")
  email = request.Post.get("email")
  senha = request.Post.get("senha")

  if len(username.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0:
    return redirect('/auth/cadastro') 

   #variavel chamada user// trazendo os dados atráves do username

    user = User.objects.filter(username==username)

    if user.exists() :
      return redirect('/auth/cadastro') 
    
    try:
      user = User(username = username, email = email, password = senha) #instancia de usuario

      #salvando no banco de dados
      user.save()
      return redirect('/auth/logar') #redirecionando para a pagina de login
    except:
      return redirect('/auth/cadastro') #caso de algum erro, redireciona para a pagina de cadastro

  return(HttpResponse)

def logar (request):
  return HttpResponse('logar')
