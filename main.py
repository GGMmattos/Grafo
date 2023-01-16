import os

lista = []

class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def le_txt(self, dados):
        self.dados = dados
        if os.path.isfile('grafo.txt'):  # Verifica se o arquivo esá OK
            file = open('grafo.txt', 'r')

            for i in file.readlines():  # Itera por todas as linhas do arquivo
                graph = i.strip().split(' ')  # Da o split se contém 2 espaços
                self.dados.append(graph[0])
        return self.dados

    # def adiciona_aresta(self, dados):
    #         #pensando em grafos direcionados sem peso nas arestas
    #         self.grafo[dados[1]].append(dados[2])

    def mostra_lista(self):
        for i in range(self.vertices):
            print(f'{i + 1}:', end='  ')
            for j in self.grafo[i]:
                print(f'{j}   ->', end='  ')
            print(' ')


g = Grafo(5)

data = g.le_txt(lista)
print(data[1])
#g.adiciona_aresta(data)
g.mostra_lista()

# data = le_txt(lista)
#
# for i in data:
#     graph1 = i.strip().split(' ')
#     teste.append(graph1[0])
#
# print(teste)
"""
if dado[0] == 'directed':
    print("Modo Direcionado")
elif dado[0] == 'undirected':
    print("Modo Não Direcionado")
"""

# arquivo.close()

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
