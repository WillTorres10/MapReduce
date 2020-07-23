from django.http import HttpResponse
from django.shortcuts import render, redirect


def verifica(request):
    if request.user.is_authenticated:
        return render(request,'layout/main.html')
    else:
        return redirect('/usuario/acessar/')

