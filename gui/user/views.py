from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        primeiroNome = request.POST.get('pNome')
        segundoNome = request.POST.get('sNome')
        email = request.POST.get('email')
        user = request.POST.get('user')
        password = request.POST.get('passoword')
        rPassword = request.POST.get('rPassword')
        if (password == rPassword):
            user = User.objects.create_user(username=user,email=email,first_name=primeiroNome,last_name=segundoNome,password=password)
            user.save()
            resultado = 'Registrado com sucesso'
            return render(request, 'register.html', {'sucesso': resultado})
        else:
            resultado = 'As senhas não são iguais'
            return render(request, 'register.html', {'mensagem':resultado})
    else:
        return render(request, 'register.html', {'mensagem':"", 'sucesso':""})

def login(request):
    if request.method == 'POST':
        primeiroNome = request.POST.get('pNome')
        segundoNome = request.POST.get('sNome')
        email = request.POST.get('email')
        user = request.POST.get('user')
        password = request.POST.get('passoword')
        rPassword = request.POST.get('rPassword')
        if (password == rPassword):
            user = User.objects.create_user(username=user,email=email,first_name=primeiroNome,last_name=segundoNome,password=password)
            user.save()
            resultado = 'Registrado com sucesso'
            return render(request, 'register.html', {'sucesso': resultado})
        else:
            resultado = 'As senhas não são iguais'
            return render(request, 'register.html', {'mensagem':resultado})
    else:
        return render(request, 'login.html', {'mensagem':"", 'sucesso':""})