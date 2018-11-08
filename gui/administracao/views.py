from django.http import HttpResponse
from django.shortcuts import render


def verifica(request):
    if request.user.is_authenticated:
        return render(request,'layout/master.html')
    else:
        return HttpResponse("Visitante")