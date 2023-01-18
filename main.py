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

    
    #implementar para OO
#Ajustar funções

import os
lista = []
class grafos:

    def __init__(self,dados=None,  dicionario_grafo=None): #Sendo none não pe obrigadtório passalos ao fazer ao fazer uma instancia
        if dicionario_grafo is None:
            dicionario_grafo = {}
            dados = []
        self.dicionario_grafo = dicionario_grafo
        self.dados = dados

    def import_graph(self, modo=None ):
        self.modo = modo
        if os.path.isfile('grafo.txt'):  # Verifica se o arquivo esá OK
            file = open('grafo.txt', 'r')

            for i in file.readlines():  # Itera por todas as linhas do arquivo
                graph = i.strip().split('  ')  # Da o split se contém 2 espaços
                self.dados.append(graph[0])
            file.close()

        self.modo = self.dados[0]
        print(self.modo)
        del (self.dados[0])
        print('salve')
        if modo == 'undirected':
            print('salve')
            for i in range(0, len(self.dados) - 1):
                self.dicionario_grafo[self.dados[i][0]] = list()
                self.dicionario_grafo[self.dados[i][2]] = list()

            for i in range(0, len(self.dados) - 1):
                if i not in self.dicionario_grafo:
                    self.dicionario_grafo[self.dados[i][0]].append(self.dados[i][2])
                    self.dicionario_grafo[self.dados[i][2]].append(self.dados[i][0])
            print(self.dicionario_grafo)
            print('salve')

        elif modo == 'directed':

            for i in range(0, len(self.dados) - 1):
                self.dicionario_grafo[self.dados[i][0]] = list()
                self.dicionario_grafo[self.dados[i][2]] = list()

            for i in range(0, len(self.dados) - 1):
                self.dicionario_grafo[self.dados[i][0]].append(self.dados[i][2])

            print(self.dicionario_grafo)


        return self.dados


g = grafos()

c = g.import_graph()





# if modo == 'undirected':
#     print("Modo Não Direcionado")
#
#     for i in range(0, len(dado) - 1):
#         listaAdjascente[dado[i][0]] = list()
#         listaAdjascente[dado[i][2]] = list()
#
#     for i in range(0, len(dado) - 1):
#         if i not in listaAdjascente:
#             listaAdjascente[dado[i][0]].append(dado[i][2])
#             listaAdjascente[dado[i][2]].append(dado[i][0])
#
# elif modo == 'directed':
#     print("Modo Direcionado")
#
#     for i in range(0, len(dado) - 1):
#         listaAdjascente[dado[i][0]] = list()
#         listaAdjascente[dado[i][2]] = list()
#
#     for i in range(0, len(dado) - 1):
#         listaAdjascente[dado[i][0]].append(dado[i][2])
#     print("Modo Não Direcionado")
#     print(listaAdjascente)
#
#
# for k, v in listaAdjascente.items(): #mostra grafo
#     print(f'{k} -> {v}')

    for i in range(0, len(dado) - 1):
        listaAdjascente[dado[i][0]] = list()
        listaAdjascente[dado[i][2]] = list()

    for i in range(0, len(dado) - 1):
        listaAdjascente[dado[i][0]].append(dado[i][2])
    print("Modo Não Direcionado")
    print(listaAdjascente)

for k, v in listaAdjascente.items():
    print(f'{k} -> {v}')
