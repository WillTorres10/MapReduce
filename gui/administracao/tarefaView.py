from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from .models import tarefa, tarefapalavras, pilhaprocessos
import json

def cadastrarPOST(request):
    job = tarefa()
    job.titulo = request.POST.get('titulo')
    job.conteudo = request.POST.get('conteudo')
    job.save()
    verficar = request.POST.get('keys')
    for palavra in verficar.split(','):
        pala = tarefapalavras()
        pala.id_tarefa = job
        pala.palavra = palavra
        pala.save()
    pilhaProcesso = pilhaprocessos()
    pilhaProcesso.id_tarefa = job
    pilhaProcesso.status_processo = 0
    pilhaProcesso.save()
    return render(request, "tarefa/cadastrar.html", {'mensagem': "Cadastro feito sucesso. Verifique o status: ", 'tipo': "success"})

def cadastrarGET(request):
    return render(request, "tarefa/cadastrar.html", {'mensagem': "", 'tipo': ""})

def cadastrarRequest(request):
    if request.method == "POST":
        return cadastrarPOST(request)
    else:
        return cadastrarGET(request)
#############################################################
def gerarStringPalavras(palavras):
    pala = ""
    for pal in palavras:
        if pala != "":
            pala += ", "+pal.palavra
        else:
            pala += pal.palavra
    return pala

@csrf_exempt
def carregarTarefaModal(request):
    idTarefa = request.POST.get('id')
    ta = tarefa.objects.get(id=idTarefa)
    palavras = gerarStringPalavras(tarefapalavras.objects.filter(id_tarefa=idTarefa))
    taPilha = pilhaprocessos.objects.get(id_tarefa=idTarefa)
    if taPilha.status_processo == 0:
        mensagem = render_to_string('ajax/listarTarefa.html', {'tarefa': ta, 'pilha':taPilha, 'palavras': palavras})
        return JsonResponse({'html' :mensagem, 'titulo': ta.titulo})
    else:
        pals = tarefapalavras.objects.filter(id_tarefa=idTarefa)
        palavrasResult = list()
        for p in pals:
            palavrasResult.append({'palavra':p.palavra, 'vezes': p.vezes})
        mensagem = render_to_string('ajax/listarTarefa.html', {'tarefa': ta, 'pilha':taPilha, 'palavras': palavras, 'resultado': palavrasResult})
        return JsonResponse({'html' :mensagem, 'titulo': ta.titulo})

def carregarVizualizacaoGet(tarefas):
    retorno = list()
    for i in tarefas:
        status = "primary"
        pilha = pilhaprocessos.objects.get(id_tarefa_id=i.id)
        if pilha.status_processo == 1:
            status = "success"
        retorno.append({'id': i.id, 'titulo': i.titulo, 'conteudo': i.conteudo, 'status': status})
    return  retorno

def visualizarTarefa(request):
    enviar = carregarVizualizacaoGet(tarefa.objects.all())
    return render(request, 'tarefa/listarTarefa.html', {'tarefa': enviar})
#############################################################
def listarComputadores(request):
    tarefas = tarefa.objects.all()
    return render(request, 'computador/listarComputador.html', {'tarefa': tarefas})

def carregarTarefa(idTarefa):
    tf = tarefa.objects.filter(id=idTarefa).first()
    palavras = list()
    pala = tarefapalavras.objects.filter(id_tarefa=idTarefa).values()
    for pa in pala:
        pa['palavra'].replace(' ', '')
        palavras.append({'id':pa['id'], "palavra":pa['palavra']})
    return {'idTarefa': tf.id, 'conteudo': tf.conteudo, 'palavras': palavras}

@csrf_exempt
def verificarTarefas(request):
    abertos = pilhaprocessos.objects.filter(status_processo=0).values()
    if abertos:
        trabalhos = list()
        for job in abertos:
            trabalhos.append(carregarTarefa(job['id_tarefa_id']))
        return JsonResponse({'tarefas': True, 'trabalhos': trabalhos})
    else:
        return JsonResponse({'tarefas': False})
@csrf_exempt
def salvarPalavras(request):
    palavras = request.POST.get('palavras')
    palavrasDict = json.loads(palavras)
    idTrabalho = 0
    for i in palavrasDict:
        print(i)
        pal = tarefapalavras.objects.get(id=i['idPalavra'])
        idTrabalho = pal.id_tarefa_id
        pal.vezes = i['quantidade']
        pal.save()
    print(idTrabalho)
    pil = pilhaprocessos.objects.filter(id_tarefa_id=idTrabalho).first()
    pil.status_processo = 1
    pil.save()
    return HttpResponse('nada')