import socket
from comunicacao.server.threadServer import threadServer

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

HOST = '10.180.14.5'              # Endereco IP do Servidor
PORT = 8001                       # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
print(HOST+":"+str(PORT)+" está funcionando")
conectados = list()
while True:
    conectados = verificaThreads(conectados)
    print("Maquinas Conectadas: "+str(len(conectados)))
    con, cliente = tcp.accept()
    th = threadServer(con, cliente)
    th.start()
    conectados.append(th)

