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
        self.tarefasExecutando = list()

    def verificaThreads(self):
        for con in self.threads:
            if not con['thread'].isAlive():
                requests.post('http://localhost:8000/administracao/computador/offStatus', data={"ip": con['ip']})
                self.threads.remove(con)

    def escolherMelhorMaquina(self):
        calculos = list()
        for th in self.threads:
            calculos.append({'thread': th['thread'], 'calculo': ((th['thread'].cpu*2 + th['thread'].ram*1)/3)})
        calculos = sorted(calculos, key=lambda k: k['calculo'])
        return calculos[0]['thread']

    def run(self):
        while True:
            self.verificaThreads()
            if len(self.threads) > 0:
                print('Verificando tarefas')
                resposta = requests.post('http://localhost:8000/administracao/tarefa/verificarTerfas')
                resposta = resposta.json()
                if resposta['tarefas']:
                    for job in resposta['trabalhos']:
                        if job not in self.tarefasExecutando:
                            maquina = self.escolherMelhorMaquina()
                            maquina.enviarTrabalho(job)
                            self.tarefasExecutando.append(job)
                        else:
                            pass
            time.sleep(2)