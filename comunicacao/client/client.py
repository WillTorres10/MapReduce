import socket, time
from comunicacao.shared.statusPC import status
import _pickle as cPickle

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 8001            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
msg = "dsdfsdfsdf"
msgS = cPickle.dumps(msg)
tcp.send(msgS)
while True:
    try:
        msg = status()
        msgS = cPickle.dumps(msg)
        tcp.send(msgS)
        time.sleep(1)
    except:
        print("Conexão com o servidor Finalizada!")
        break
tcp.close()