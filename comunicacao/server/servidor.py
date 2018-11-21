import socket, _thread, time
from comunicacao.server.threadServer import threadServer
from comunicacao.server.resolverProblemas.verificarTarefa import verificarTarefa

class servidor:

    def __init__(self):
        self.HOST = '10.180.84.20'  # Endereco IP do Servidor
        self.PORT = 8002  # Porta que o Servidor esta
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.orig = (self.HOST, self.PORT)
        self.tcp.bind(self.orig)
        self.tcp.listen(1)
        print(self.HOST + ":" + str(self.PORT) + " está funcionando")
        self.conectados = list()
        self.execultar()

    def execultar(self):
        tarefa = verificarTarefa(self.conectados)
        tarefa.start()
        while True:
            con, cliente = self.tcp.accept()
            th = threadServer(con, cliente)
            th.start()
            self.conectados.append({'thread':th,'ip':th.retornarIP()})
servidor()