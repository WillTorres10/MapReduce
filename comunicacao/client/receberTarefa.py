import threading, _pickle as cPickle
from comunicacao.client.realizarTarefa import realizarTarefa

'''
    /------------------------------------------------------------------------------------------------------------------/
    FALTA
    /------------------------------------------------------------------------------------------------------------------/
        - Nada
    /------------------------------------------------------------------------------------------------------------------/
    FUNÇÃO
    /------------------------------------------------------------------------------------------------------------------/
    Essa classe é a thread responsável por receber os trabalhos enviados pelo servidor e criar uma nova thread pare 
    resolver o trabalho enviado pelo servidor
    /------------------------------------------------------------------------------------------------------------------/
'''

class receberTarefa(threading.Thread):

    def __init__(self, conexao):
        print("Pronto para receber Tarefa")
        threading.Thread.__init__(self)
        self.con = conexao

    def run(self):
        while True:
            trabalho = cPickle.loads(self.con.recv(1024))
            rt = realizarTarefa(trabalho, self.con)
            rt.start()