from django.db import models

# Create your models here.
from django.db import models

class computador(models.Model):
    nome = models.CharField(max_length=50)
    ip = models.CharField(max_length=50)
    chave = models.CharField(max_length=100)
    status = models.IntegerField()

class computadorstatus(models.Model):
    processador = models.FloatField()
    ram = models.FloatField()
    id_pc = models.ForeignKey(computador, models.DO_NOTHING)

class pilhaprocessos(models.Model):
    status_processo = models.IntegerField()
    tempo = models.FloatField(default=0.0)
    id_tarefa = models.ForeignKey('tarefa', models.DO_NOTHING)

class tarefa(models.Model):
    titulo = models.CharField(max_length=50)
    conteudo = models.CharField(max_length=10000)

class tarefapalavras(models.Model):
    palavra = models.CharField(max_length=50)
    vezes = models.IntegerField(default=0)
    id_tarefa = models.ForeignKey(tarefa, models.DO_NOTHING)