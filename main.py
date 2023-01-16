import os
lista = []
teste = []

def le_txt(dados):

    if os.path.isfile('grafo.txt'): #Verifica se o arquivo esá OK
        file = open('grafo.txt', 'r')

        for i in file.readlines(): #Itera por todas as linhas do arquivo
            graph = i.strip().split(' ') #Da o split se contém 2 espaços
            dados.append(graph[0])
    print(dados)
    return dados

def adiciona_aresta():
            #pensando em grafos direcionados sem peso nas arestas
            self.grafo[u-1].append(v)

data = le_txt(lista)

for i in data:
    graph1 = i.strip().split(' ')
    teste.append(graph1[0])

print(teste)
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
