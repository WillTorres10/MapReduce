from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.http import JsonResponse

from .models import computador

@csrf_exempt
def cadastrarPOST(request):
    pc = computador()
    pc.nome = request.POST.get('name')
    pc.ip = request.POST.get('ip')
    pc.chave = request.POST.get('chave')
    pc.status = True
    pc.save()
    mensagem = "Máquina com o IP: " + pc.ip +" cadastrado com sucesso!"
    return render(request, 'computador/cadastrar.html', {'mensagem':mensagem, 'tipo':"success"})

def cadastrarGET(request):
    return render(request, 'computador/cadastrar.html', {'mensagem':"", 'tipo':""})

def cadastrarRequest(request):
    if request.method == 'POST':
        return cadastrarPOST(request)
    else:
        return cadastrarGET(request)

def listarComputadores(request):
    pc = computador.objects.all()
    return render(request, 'computador/listarComputador.html', {'pc':pc})

def recuperarDadosComputador(request):
    print("aaaaaaaaaa")
    idComputador = request.POST.get('idComputador')
    comp = computador.objects.get(id=idComputador)
    html = render_to_string('ajax/listarComputador.html', {'computador': comp})
    return JsonResponse({'html':html, 'titulo':comp.nome})
