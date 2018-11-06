from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from .forms import *
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


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

@csrf_exempt
def acessar(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('administracao:padrao')
    else:
        if request.method == 'POST':
            userName = request.POST.get('user')
            password = request.POST.get('pass')
            user = authenticate(username=userName, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'login.html', {'mensagem': "", 'sucesso': "Logado com sucesso"})
            else:
                return render(request, 'login.html', {'mensagem': "Erro ao autenticar, verifique suas credenciais", 'sucesso': ""})
        else:
            return render(request, 'login.html', {'mensagem': "", 'sucesso': ""})