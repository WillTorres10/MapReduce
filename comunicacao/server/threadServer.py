import _pickle as cPickle, requests
class threadServer:
    def __init__(self, con, client):
        self.con = con
        self.cliente = client

    def executa(self):
        print ('Conectado por', self.cliente[0])
        chaveS = self.con.recv(4000)
        chave = cPickle.loads(chaveS)
        resposta = requests.post('http://localhost:8000/administracao/computador/validaPC', data={"chave":chave, 'ip':self.cliente[0]})
        dados = resposta.json()
        if dados['valido'] == True:
            while True:
                msgS = self.con.recv(4000)
                msg = cPickle.loads(msgS)
                if not msg: break
                print(self.cliente,'= RAM: '+str(msg['ram'])+'% | CPU: '+str(msg['cpu'])+'%')
        else:
            print(self.cliente, 'Não é um computador do cluster!')
        self.con.close()
        print ('Finalizando conexao do cliente', self.cliente)