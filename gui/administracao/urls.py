from django.http import HttpResponse
from django.urls import path
from . import views, computadorView, tarefaView

app_name = 'administracao'
urlpatterns = [
    path('', views.verifica, name="home"),
    path('computador/cadastrar', computadorView.cadastrarRequest, name="cadastrarPC"),
    path('computador/listar', computadorView.listarComputadores, name="listarPC"),
    path('tarefa/cadastrar', tarefaView.cadastrarRequest, name="cadastrarTarefa"),

    path('ajax/dadosComputador', computadorView.recuperarDadosComputador, name="recuperaPC"),
]