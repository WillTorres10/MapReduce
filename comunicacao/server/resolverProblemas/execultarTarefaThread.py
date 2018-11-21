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
import threading, _pickle as cPickle1, json, requests, time, pickle as cPickle

class execultarTarefaThread(threading.Thread):

    def __init__(self, con, tarefa):
        threading.Thread.__init__(self)
        self.maquina = con
        self.tarefa = tarefa

    def run(self):
        start_time = time.time()
        enviar = cPickle.dumps(self.tarefa, protocol=cPickle.HIGHEST_PROTOCOL)
        self.maquina.sendall(enviar)
        print("enviado")
        while True:
            retorno = cPickle.loads(self.maquina.recv(4028))
            try:
                if retorno[0]['tipo'] == 'retorno':
                    enviar = json.dumps(retorno)
                    end_time = time.time()

                    resposta = requests.post('http://localhost:8000/administracao/tarefa/salvarTarefa',
                                             data={
                                                 "palavras": enviar,
                                                 'tempo': (end_time-start_time)
                                               })
                    print("Resolvido")
                    break
            except:
                continue