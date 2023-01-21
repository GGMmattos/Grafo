import os

class grafos:
    def __init__(self, dados=None, dicionario_grafo=None, vertices=None, directed=False, teste=None):  # Sendo none não é obrigadtório passalos ao fazer uma instancia
        if dicionario_grafo is None:
            dicionario_grafo = {}
            dados = []
        self.dicionario_grafo = dicionario_grafo
        self.dados = dados
        self.teste = teste
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

    def mostra_matriz_adjacencia(self, Quant_vertice=None, matriz=None):
        self.Quant_vertice = len(self.dicionario_grafo)
        self.matriz = [[0] * self.Quant_vertice for i in range(self.Quant_vertice)]  # criação da matriz que só tem zero

        ordenada = g.elementos_ordenados()
        dados = g.dados

        for i in range(0, len(dados)):
            # self.matriz[0][2] = 1
            # self.matriz[ordenada.index('a')][ordenada.index('c')] = 1
            self.matriz[ordenada.index(dados[i][0])][ordenada.index(dados[i][2])] = 1
        for i in range(len(self.dicionario_grafo)):
            print(self.matriz[i])

    # def adiciona_arestas(self): #arestas U e V
    #
    #     print(self.dados[0])

    def inserir_vertice(self, vertice):
        self.vertices = vertice
        if self.vertices not in self.dicionario_grafo:
            key = self.vertices #adiciona nova aresta
            self.dicionario_grafo[key] = list()
            print(f'O vertice {self.vertices} foi adicionado!!! ')
        else:
            print(f'O vertice {self.vertices} já faz parte do grafo!!!')

    def inserir_aresta(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

        #Para grafos não direcionados
        if self.v1 not in self.dicionario_grafo:
            print(f'A aresta {self.v1} não faz parte do grafo!!!')

        elif self.v2 not in self.dicionario_grafo:
            print(f'{self.v2} não faz parte do grafo!!!')

        elif self.v2 in self.dicionario_grafo[self.v1]:
            print('Aresta ja exite!!!')
        else:
            if self.directed:
                self.dicionario_grafo[self.v1].append(self.v2)  #a->b
            else:
                self.dicionario_grafo[self.v1].append(self.v2)  #a->b
                self.dicionario_grafo[self.v2].append(self.v1)  #b->a

    def remover_vertice(self, vertice):
        #tratar vertice ja removido
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

    def elementos_ordenados(self):
        lista_elementos = list()
        for i in range(0, len(self.dados)):
            if self.dados[i][0] not in lista_elementos:
                lista_elementos.append(self.dados[i][0])
            if self.dados[i][2] not in lista_elementos:
                lista_elementos.append(self.dados[i][2])
        lista_elementos.sort()
        return lista_elementos


g = grafos()
d = g.import_graph()
# elementos = g.cria_lista_elementos()
# print(elementos)
g.mostra_matriz_adjacencia()
# g.mostra_grafo()
#
# g.mostra_matriz_adjacencia()

#conversão de letras em números, creio que de para utilizar

# l = "abcde"
# n = []
# for x in l:
#    n.append(ord(x) - 96)
# print(n)
