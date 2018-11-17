import _pickle as cPickle, requests
import threading


class threadServer(threading.Thread):
    ram = 0.0
    cpu = 0.0
    def __init__(self, con, client):
        threading.Thread.__init__(self)
        self.con = con
        self.cliente = client

    def run(self):
        chaveS = self.con.recv(4000)
        chave = cPickle.loads(chaveS)
        resposta = requests.post('http://localhost:8000/administracao/computador/validaPC', data={"chave":chave, 'ip':self.cliente[0]})
        dados = resposta.json()
        if dados['valido'] == True:
            try:
                while True:
                    msgS = self.con.recv(4000)
                    msg = cPickle.loads(msgS)
                    self.ram = msg['ram']
                    self.cpu = msg['cpu']
                    resposta = requests.post('http://localhost:8000/administracao/computador/salvaStatus',
                                             data={
                                                 "chave": chave,
                                                 'ip': self.cliente[0],
                                                 'cpu':msg['cpu'],
                                                 'ram':msg['ram']
                                               })
            except:
                self.con.close()
        else:
            print(self.cliente, 'Não é um computador do cluster!')
        self.con.close()