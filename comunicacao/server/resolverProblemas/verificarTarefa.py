'''
    /------------------------------------------------------------------------------------------------------------------/
    FALTA
    /------------------------------------------------------------------------------------------------------------------/
        - Nada
    /------------------------------------------------------------------------------------------------------------------/
    FUNÇÃO
    /------------------------------------------------------------------------------------------------------------------/
    Essa classe é uma thread que é iniciada quando o servido é ligado. Sua função é ficar verificando a cada 5 segundos
    se há algum trabalho no banco de dados que ainda não foi feito. Se houver ela escolherá a máquina com mais recurso
    livre e então envia o trabalho para ele.
    /------------------------------------------------------------------------------------------------------------------/
'''
import threading, time, requests

class verificarTarefa(threading.Thread):

    def __init__(self, threads):
        threading.Thread.__init__(self)
        self.threads = threads

    def escolherMelhorMaquina(self):
        calculos = list()
        for th in self.threads:
            calculos.append({'thread': th, 'calculo': ((th.cpu*2 + th.ram*1)/3)})
        calculos.sort(key=lambda x: x[1])
        return calculos[0]['thread']

    def run(self):
        resposta = requests.post('http://localhost:8000/administracao/tarefa/verificarTerfas')
        print(resposta.content)
        resposta = resposta.json()
        if resposta['tarefas']:
            for job in resposta['trabalhos']:
                maquina = self.escolherMelhorMaquina()[0]
                maquina.enviarTrabalho(job)
        time.sleep(5)