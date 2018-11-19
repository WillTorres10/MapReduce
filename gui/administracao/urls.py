from django.http import HttpResponse
from django.urls import path
from . import views, computadorView, tarefaView

app_name = 'administracao'
urlpatterns = [
    path('', views.verifica, name="home"),
    path('computador/cadastrar', computadorView.cadastrarRequest, name="cadastrarPC"),
    path('computador/listar', computadorView.listarComputadores, name="listarPC"),
    path('computador/validaPC', computadorView.validaComputador, name="validaPC"),
    path('computador/salvaStatus', computadorView.salvarStatusComputador, name="statusPC"),

    path('tarefa/cadastrar', tarefaView.cadastrarRequest, name="cadastrarTarefa"),
    path('tarefa/visualizarTarefa', tarefaView.visualizarTarefa, name="visualizarTarefa"),
    path('tarefa/verificarTerfas', tarefaView.verificarTarefas, name="verificarTarefa"),

    path('ajax/dadosComputador', computadorView.recuperarDadosComputador, name="recuperaPC"),
    path('ajax/atualizarComputador', computadorView.atualizarDadosComputador, name="atualizarPC"),
    path('ajax/deletarComputador', computadorView.excluirComputador, name="deletarPC"),
    path('ajax/dadosTarefa', tarefaView.carregarTarefaModal, name="recuperaTarefa"),
]