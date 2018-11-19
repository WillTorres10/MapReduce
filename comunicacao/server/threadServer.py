"""
    /------------------------------------------------------------------------------------------------------------------/
    FALTA
    /------------------------------------------------------------------------------------------------------------------/
        - Criar thread para ficar salvando os status da máquina
    /------------------------------------------------------------------------------------------------------------------/
    FUNÇÃO
    /------------------------------------------------------------------------------------------------------------------/
    Classe responsável por lidar com as máquinas que estão conectadas com o servidor. Ela autentica as conexão, quando
    a conexão está autenticada ela fica enviando os status do computador para o banco de dados do sistema e fica
    aguardando a chamada para criar a thread para lidar com um trabalho.
    /------------------------------------------------------------------------------------------------------------------/
"""
import _pickle as cPickle, requests
import threading
from .resolverProblemas.execultarTarefaThread import execultarTarefaThread

class threadServer(threading.Thread):
    ram = 0.0
    cpu = 0.0
    def __init__(self, con, client):
        threading.Thread.__init__(self)
        self.con = con
        self.cliente = client

    def enviarTrabalho(self, trabalho):
        th = execultarTarefaThread(self.con, trabalho)
        th.start()

    def run(self):
        chave = cPickle.loads(self.con.recv(4000))
        resposta = requests.post('http://localhost:8000/administracao/computador/validaPC', data={"chave":chave, 'ip':self.cliente[0]})
        dados = resposta.json()
        if dados['valido'] == True:
            try:
                while True:
                    msg = cPickle.loads(self.con.recv(4000))
                    self.ram = msg['ram']
                    self.cpu = msg['cpu']
                    resposta = requests.post('http://localhost:8000/administracao/computador/salvaStatus',
                                             data={
                                                 "chave": chave,
                                                 'ip': self.cliente[0],
                                                 'cpu': msg['cpu'],
                                                 'ram': msg['ram']
                                               })
            except:
                self.con.close()
        else:
            print(self.cliente, 'Não é um computador do cluster!')
        self.con.close()