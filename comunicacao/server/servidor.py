import socket, _thread
from comunicacao.server.threadServer import threadServer

HOST = '127.0.0.1'              # Endereco IP do Servidor
PORT = 8001                     # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
print(HOST+":"+str(PORT)+" está funcionando")
while True:
    con, cliente = tcp.accept()
    th = threadServer(con, cliente)
    _thread.start_new_thread(th.executa, tuple([]))
