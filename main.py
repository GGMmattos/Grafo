# import os
# import sys
#
# #Para checar e ler o segundo argumento da chamada como txtGrafo (txtGrafo: nome do arquivo txt)
# if (len(sys.argv) == 2):
#     txtGrafo = sys.argv[1]
# else:
#     print ("falta arquivo txt como segundo argumento da chamada, ex: (python graph.py arquivo.txt)")
#     exit()
#
# #lista auxilio so pra exemplo
# aux = []
# class grafo:
#
#     def init(self, dicionario_grafo=None):
#         if dicionario_grafo is None:
#             dicionario_grafo = {}
#         self.dicionario_grafo = dicionario_grafo
#
#     def le_txt(self, dados):
#         self.dados = dados
#         if os.path.isfile(txtGrafo):
#             file = open(txtGrafo, 'r')
#
#             for i in file.readlines():
#                 graph = i.strip().split(' ')
#                 self.dados.append(graph[0])
#             print(dados)
#         else:
#             print ("error")
#         return self.dados
#
#
# g = grafo(aux)
#
#
# g.le_txt(aux)


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
# class Grafo:


# with open ('grafo.txt', 'r') as arquivo:
#     grafo = arquivo.read()
#     print(grafo)

# vertices =grafo.split()
# print(vertices)


# GRAFO = { 'A': [],
#           'B': ['A', 'E'],
#           'C': ['D', 'B'],
#           'D': ['B'],
#           'E': ['D', 'B']
# }
