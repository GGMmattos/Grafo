import os

class grafos:

    def __init__(self, dados=None, dicionario_grafo=None, vertices=None, directed=False):  # Sendo none não é obrigadtório passalos ao fazer uma instancia
        if dicionario_grafo is None:
            dicionario_grafo = {}
            dados = []
        self.dicionario_grafo = dicionario_grafo
        self.dados = dados
        self.vertices = vertices
        self.directed = directed

    def import_graph(self, modo=None):
        self.modo = modo

        if os.path.isfile('grafo.txt'):  # Verifica se o arquivo esá OK
            file = open('grafo.txt', 'r')
            for i in file.readlines():  # Itera por todas as linhas do arquivo
                graph = i.strip().split('  ')  # Da o split se contém 2 espaços
                self.dados.append(graph[0])
            file.close()

        self.modo = self.dados[0] #captura do "tipo" do grafo
        del (self.dados[0])

        if self.modo == 'undirected':
            for i in range(0, len(self.dados) - 1):
                self.dicionario_grafo[self.dados[i][0]] = list()
                self.dicionario_grafo[self.dados[i][2]] = list()

            for i in range(0, len(self.dados) - 1):
                if i not in self.dicionario_grafo:
                    self.dicionario_grafo[self.dados[i][0]].append(self.dados[i][2])
                    self.dicionario_grafo[self.dados[i][2]].append(self.dados[i][0])

        elif self.modo == 'directed':
            self.directed = True
            for i in range(0, len(self.dados)): #foi ajustado não estava iterando commpletamente
                self.dicionario_grafo[self.dados[i][0]] = list()
                self.dicionario_grafo[self.dados[i][2]] = list()

            for i in range(0, len(self.dados)): #foi ajustado não estava iterando commpletamente
                self.dicionario_grafo[self.dados[i][0]].append(self.dados[i][2])

        return self.dicionario_grafo

    def mostra_grafo(self):
        for k, v in self.dicionario_grafo.items():
            print(f'{k}: {v}')

    def mostra_matriz_adjacencia(self, vertices, matriz=None):
        self.vertices = vertices
        self.matriz = [[0] * self.vertices for i in range(self.vertices)]  # criação da matriz que só tem zero
        for i in range(self.vertices):
            print(self.matriz[i])
        #OBS será implementada a inserção das arestas na matriz

    def inserir_vertice(self, vertice):
        self.vertices = vertice
        if self.vertices not in self.dicionario_grafo:
            key = self.vertices
            self.dicionario_grafo[key] = list()
            print(f'O vertice {self.vertices} foi adicionado!!! ')
        else:
            print(f'O vertice {self.vertices} já faz parte do grafo!!!')

    def inserir_aresta(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

        #Para grafos não direcionados
        if self.v1 not in self.dicionario_grafo:
            print(f'{self.v1} não faz parte do grafo!!!')

        elif self.v2 not in self.dicionario_grafo:
            print(f'{self.v2} não faz parte do grafo!!!')

        elif self.v2 in self.dicionario_grafo[self.v1]:
            print('Aresta ja exite!!!')
        else:
            if self.directed:
                self.dicionario_grafo[self.v1].append(self.v2)
            else:
                self.dicionario_grafo[self.v1].append(self.v2)
                self.dicionario_grafo[self.v2].append(self.v1)

    def remover_vertice(self, vertice):
        self.dicionario_grafo.pop(vertice) #remoção da vertice
        for k, v in self.dicionario_grafo.items(): #remoção geral da vertice(exclusão das arestas)
            if vertice in v:
                del v[v.index(vertice)]

    def remover_aresta(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

        for k, v in self.dicionario_grafo.items():
            if k == self.v1:
                del v[v.index(self.v2)]



g = grafos()
d = g.import_graph()
g.inserir_aresta('c', 'a')
g.inserir_aresta('d', 'a')
g.inserir_aresta('e', 'a')

g.mostra_grafo()
# g.inserir_vertice('f')
# g.inserir_vertice('g')
# g.inserir_vertice('f')
# g.inserir_aresta('a', 'f')
# g.inserir_aresta('a', 'g')
print(' ')
g.remover_vertice('a')
g.remover_aresta('b','d')
g.remover_aresta('b','e')
g.mostra_grafo()



#g.mostra_matriz_adjacencia(len(d))
#conversão de letras em números, creio que de para utilizar

# l = "a b c"
# n = []
# for x in l:
#    n.append(ord(x) - 96)
# print(n)
