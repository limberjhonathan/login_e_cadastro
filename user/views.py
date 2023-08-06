from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def home(request):
    return render(
        request,
        'home/home.html'
    )

def cadastro(request):
    print(request.method)

    if request.method == 'GET':
        return render(
            request,
            'home/cadastro.html'
            )
    # print(request.POST)
    username = request.POST.get('user')
    email = request.POST.get('email')
    senha = request.POST.get('password')
    print(f'Nome: {username}, \nEmail: {email}, \nPassword: {senha}')

    user = User.objects.filter(username=username).first()
    if user:
        login(request, user)
        return HttpResponse("Este usuario ja existe")
    
    user = User.objects.create_user(username=username, email=email, password=senha)
    user.save()
    return HttpResponse("Cadastro realizado com sucesso")

    print(user)

def login_user(request):
    if request.method == 'GET':
        return render(
            request,
            'home/login.html'
        )

    username = request.POST.get('user')
    senha = request.POST.get('password')
    
    print(username, senha)
    user = authenticate(username=username, password=senha)
    if user:
        return render(
            request,
            'templates/login_success.html'
        )

# so sera diresionado se estiver logado
@login_required
def plataforma(request):
    # if request.user.is_authenticated:
    #     return HttpResponse("Usuário logados com sucesso")
    return HttpResponse("E necessario estar logado")