from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import tarefa, tarefapalavras

@csrf_exempt
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
    return render(request, "tarefa/cadastrar.html", {'mensagem': "Cadastro feito sucesso. Verifique o status: ", 'tipo': "success"})

def cadastrarGET(request):
    return render(request, "tarefa/cadastrar.html", {'mensagem': "", 'tipo': ""})

def cadastrarRequest(request):
    if request.method == "POST":
        return cadastrarPOST(request)
    else:
        return cadastrarGET(request)

def listarComputadores(request):
    tarefas = tarefa.objects.all()
    return render(request, 'computador/listarComputador.html', {'tarefa': tarefas})