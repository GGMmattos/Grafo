import os
lista = []


def le_txt(dados):
    if os.path.isfile('grafo.txt'):  # Verifica se o arquivo esá OK
        file = open('grafo.txt', 'r')
        for i in file.readlines():  # Itera por todas as linhas do arquivo
            graph = i.strip().split('  ')  # Da o split se contém 2 espaços
            dados.append(graph[0])
        file.close()
    return dados


dado = le_txt(lista)
modo = dado[0]
del (dado[0])

listaAdjascente = {}

if modo == 'undirected':
    for i in range(0, len(dado) - 1):
        listaAdjascente[dado[i][0]] = list()
        listaAdjascente[dado[i][2]] = list()

    for i in range(0, len(dado) - 1):
        if i not in listaAdjascente:
            listaAdjascente[dado[i][0]].append(dado[i][2])
            listaAdjascente[dado[i][2]].append(dado[i][0])

    print(listaAdjascente['a'])
    print("Modo Direcionado")

elif modo == 'directed':

    for i in range(0, len(dado) - 1):
        listaAdjascente[dado[i][0]] = list()
        listaAdjascente[dado[i][2]] = list()

    for i in range(0, len(dado) - 1):
        listaAdjascente[dado[i][0]].append(dado[i][2])
    print("Modo Não Direcionado")
    print(listaAdjascente)

for k, v in listaAdjascente.items():
    print(f'{k} -> {v}')
