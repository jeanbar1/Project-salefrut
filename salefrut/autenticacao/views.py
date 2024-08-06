from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse

def login_view(request):
    if request.method == 'GET':
        return render(request, 'autenticacao/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponse('autenticado')
        else:
            return HttpResponse('email ou senha invalida')
def plataforma_view(request):
    if request.user.is_authenticated:
        return HttpResponse('Plataforma')
    return HttpResponse('Você precisa estar logado')

def logout_view(request):
    logout(request)
    return redirect('login')

def cadastro_view(request):
    if request.method == 'GET':
        return render(request, 'autenticacao/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username já cadastrado")
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        return HttpResponse('Cadastrado com sucesso')
