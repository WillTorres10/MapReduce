import socket
from comunicacao.server.threadServer import threadServer
from comunicacao.server.resolverProblemas.verificarTarefa import verificarTarefa

def verificaThreads(conectados):
    mortos = list()
    for con in conectados:
        if not con.isAlive():
            cont = conectados.index(con)
            mortos.append(cont)
    try:
        for i in mortos:
            conectados.pop(i)
    except:
        return conectados
    return conectados

HOST = '192.168.0.100'              # Endereco IP do Servidor
PORT = 8001                       # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
print(HOST+":"+str(PORT)+" está funcionando")
conectados = list()
tarefa = verificarTarefa(conectados)
tarefa.start()
while True:
    conectados = verificaThreads(conectados)
    con, cliente = tcp.accept()
    th = threadServer(con, cliente)
    th.start()
    conectados.append(th)

