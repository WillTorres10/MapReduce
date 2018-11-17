from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.http import JsonResponse

from .models import computador

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
    idComputador = request.POST.get('idComputador')
    comp = computador.objects.get(id=idComputador)
    html = render_to_string('ajax/listarComputador.html', {'computador': comp})
    return JsonResponse({'html':html, 'titulo':comp.nome})

def atualizarDadosComputador(request):
    idComputador = request.POST.get('idComputador')
    comp = computador.objects.get(id=idComputador)
    comp.nome = request.POST.get('nome')
    comp.ip = request.POST.get('ip')
    comp.chave = request.POST.get('chave')
    comp.save()
    html = '<div class="alert alert-success" role="alert">Máquina atualizada com sucesso!</div>'
    return JsonResponse(html, safe=False)

def excluirComputador(request):
    idComputador = request.POST.get('idComputador')
    comp = computador.objects.get(id=idComputador)
    comp.delete()
    html = '<div class="alert alert-success" role="alert">Máquina excluida com sucesso!</div>'
    return JsonResponse(html, safe=False)

@csrf_exempt
def validaComputador(request):
    chavePC = request.POST.get('chave')
    ipPC = request.POST.get('ip')
    # comp = computador.objects.filter(chave=chavePC)
    comp = computador.objects.filter(ip=ipPC).first()
    if comp:
        if comp.chave == chavePC:
            return JsonResponse({'valido': True}, safe=False)
        else:
            return JsonResponse({'valido': False}, safe=False)
    else:
        return JsonResponse({'valido': False}, safe=False)