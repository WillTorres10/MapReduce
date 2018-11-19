'''
    /------------------------------------------------------------------------------------------------------------------/
    FALTA
    /------------------------------------------------------------------------------------------------------------------/
        - Nada
    /------------------------------------------------------------------------------------------------------------------/
    FUNÇÃO
    /------------------------------------------------------------------------------------------------------------------/
    Essa classe enviar o trabalho para a máquina que está conectada ao servidor e recebe e salva as informações de
    retorno

    Ela é chamada a máquina recebe alguma tarefa
    /------------------------------------------------------------------------------------------------------------------/
'''
import threading, _pickle as cPickle

class execultarTarefaThread(threading.Thread):

    def __init__(self, con, tarefa):
        threading.Thread.__init__(self)
        self.maquina = con
        self.tarefa = tarefa

    def run(self):
        self.maquina.send(cPickle.dumps(self.tarefa))
        retorno = cPickle.loads(self.maquina.recv(4000))
