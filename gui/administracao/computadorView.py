from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.http import JsonResponse
import json
from django.core.serializers.json import DjangoJSONEncoder

from .models import computador, computadorstatus

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

def carregarStatusPC(idComputador):
    pc = computadorstatus.objects.filter(id_pc=idComputador).order_by('-id')[:11]
    cpu, ram = list(), list()
    if pc:
        for p in pc:
            cpu.append(p.processador)
            ram.append(p.ram)
    return json.dumps(cpu, cls=DjangoJSONEncoder), json.dumps(ram, cls=DjangoJSONEncoder)

@csrf_exempt
def carregarStatusPCRealTime(request):
    idComputador = request.POST.get('idComputador')
    pc = computadorstatus.objects.filter(id_pc=idComputador).order_by('-id')[:2]
    cpu, ram = list(), list()
    if pc:
        for p in pc:
            cpu.append(p.processador)
            ram.append(p.ram)
    return JsonResponse({'cpu':json.dumps(cpu, cls=DjangoJSONEncoder), 'ram':json.dumps(ram, cls=DjangoJSONEncoder)})

@csrf_exempt
def recuperarDadosComputador(request):
    idComputador = request.POST.get('idComputador')
    comp = computador.objects.get(id=idComputador)
    cpu, ram = carregarStatusPC(idComputador)
    html = render_to_string('ajax/listarComputador.html', {'computador': comp,})
    return JsonResponse({'html' :html, 'titulo': comp.nome,'status': comp.status, 'cpu': cpu, 'ram':ram})

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
    status = computadorstatus.objects.filter(id_pc=idComputador).delete()
    comp.delete()
    html = '<div class="alert alert-success" role="alert">Máquina excluida com sucesso!</div>'
    return JsonResponse(html, safe=False)

@csrf_exempt
def validaComputador(request):
    chavePC = request.POST.get('chave')
    ipPC = request.POST.get('ip')
    comp = computador.objects.filter(ip=ipPC).first()
    if comp:
        if comp.chave == chavePC:
            comp.status = 1
            comp.save()
            return JsonResponse({'valido': True}, safe=False)
        else:
            return JsonResponse({'valido': False}, safe=False)
    else:
        return JsonResponse({'valido': False}, safe=False)

@csrf_exempt
def statusOff(request):
    ipPC = request.POST.get('ip')
    comp = computador.objects.get(ip=ipPC)
    comp.status = 0
    comp.save()
    return HttpResponse("nada")

@csrf_exempt
def salvarStatusComputador(request):
    chavePC = request.POST.get('chave')
    ipPC = request.POST.get('ip')
    cpu = request.POST.get('cpu')
    ram = request.POST.get('ram')
    comp = computador.objects.filter(ip=ipPC).first()
    if comp:
        if comp.chave == chavePC:
            pc = computadorstatus()
            pc.id_pc = comp
            pc.processador = cpu
            pc.ram = ram
            pc.save()
    return HttpResponse('nada')