import os

class grafos:

    def __init__(self, dados=None, dicionario_grafo=None, vertices=None):  # Sendo none não é obrigadtório passalos ao fazer uma instancia
        if dicionario_grafo is None:
            dicionario_grafo = {}
            dados = []
        self.dicionario_grafo = dicionario_grafo
        self.dados = dados
        self.vertices = vertices

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


#g = grafos()
#d = g.import_graph()
#g.mostra_grafo()
#g.mostra_matriz_adjacencia(len(d))
#conversão de letras em números, creio que de para utilizar

# l = "a b c"
# n = []
# for x in l:
#    n.append(ord(x) - 96)
# print(n)
