'''
    /------------------------------------------------------------------------------------------------------------------/
    FALTA
    /------------------------------------------------------------------------------------------------------------------/
        - Retornar o resultado
    /------------------------------------------------------------------------------------------------------------------/
    FUNÇÃO
    /------------------------------------------------------------------------------------------------------------------/
    Essa classe será a thread responsável por resolver o trabalho recebido pela classe receberTarefa
    /------------------------------------------------------------------------------------------------------------------/
'''
import threading, _pickle as cPickle

class realizarTarefa(threading.Thread):

    def __init__(self, trabalho, con):
        threading.Thread.__init__(self)
        self.maquina = con
        self.conteudo = trabalho['conteudo']
        self.palavras = trabalho['palavras']
        print("Realizando Trabalho")

    def retornarResultado(self):
        self.maquina.send(cPickle.dumps(self.retorno))

    def verificarPalavras(self,ordenado, palavra):
        tem = 0
        for ord in ordenado:
            if ord[0] == palavra['palavra']:
                return ord[1]
        if tem == 0:
            return 0


    def run(self):
        elimina = [',', '.', ';', ':', '/', '!', '?']
        elimina2 = ['\r','\n']
        for eli in elimina:
            self.conteudo = self.conteudo.lower().replace(eli, '')
        for eli in elimina2:
            self.conteudo = self.conteudo.lower().replace(eli, ' ')
        existentes, contar = list(), list()
        for palavra in self.conteudo.split(" "):
            if palavra in existentes:
                contar[existentes.index(palavra)] += 1
            else:
                existentes.append(palavra)
                contar.append(1)
        ordenado = list()
        for i in range(len(existentes)):
            ordenado.append([existentes[i], contar[i]])
        ordenado.sort(key=lambda x: x[1])

        self.retorno = list()
        for pal in self.palavras:
            result = self.verificarPalavras(ordenado,pal)
            self.retorno.append({'tipo': 'retorno', 'idPalavra': pal['id'], 'quantidade': result})
        self.retornarResultado()
        print("Trabalho Escravo Finalizado")