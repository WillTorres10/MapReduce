frase = ""

with open('texto.txt', 'r') as myfile:
    frase=myfile.read().replace('\n', ' ')

existentes = list()
contar = list()

for palavra in frase.split(" "):
    if palavra in existentes:
        posicao = existentes.index(palavra)
        contar[posicao] += 1
    else:
        existentes.append(palavra)
        contar.append(1)
ordenado = list()

for i in range(len(existentes)):
    ordenado.append([existentes[i],contar[i]])

ordenado.sort(reverse=True ,key=lambda x:x[1])

print(ordenado)
