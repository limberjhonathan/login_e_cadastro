from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

def cadastro(request):
    print(request.method)
    # print(request.POST)
    username = request.POST.get('user')
    email = request.POST.get('email')
    senha = request.POST.get('password')
    # print(f'Nome: {username}, \nEmail: {email}, \nPassword: {senha}')

    user = User.objects.filter(username=username).first()
    if user:
        return HttpResponse("Este usuario ja existe")
    
    user = User.objects.create(username=username, email=email, password=senha)
    user.save()
        
    print(user)
    return render(
        request,
        'home/cadastro.html'

    )

def login(request):
    return render(
        request,
        'home/login.html'

    )

