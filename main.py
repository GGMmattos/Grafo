import os


# A complexidade de tempo analizada não leva em conta funções internas do python :)

class grafos:
    def __init__(self, dados=None, dicionario_grafo=None, vertices=None, directed=False,
                 teste=None):  # Sendo none não é obrigadtório passalos ao fazer uma instancia
        if dicionario_grafo is None:
            dicionario_grafo = {}
            dados = []
        self.dicionario_grafo = dicionario_grafo
        self.dados = dados
        self.teste = teste
        self.vertices = vertices
        self.directed = directed

    def import_graph(self, nome_grafo):
        if os.path.isfile(nome_grafo):  # Verifica se o arquivo esá OK
            file = open(nome_grafo, 'r')
            for i in file.readlines():  # Itera por todas as linhas do arquivo
                graph = i.strip().split('  ')  # Da o split se contém 2 espaços
                self.dados.append(graph[0])
            file.close()
            if self.dados[0] == 'directed':
                self.directed = True
            elif self.dados[0] == 'undirected':
                self.directed = False
            else:
                print('Primeira linha do arquivo deve ser preenchida apenas com "directed" ou "undirected"')
                exit(1)
            del (self.dados[0])
            print(self.dados)

    # Complexidade de tempo: O(n)

    def criar_dicionario(self):
        if not self.directed:
            print('nao direcionado')
            for i in range(0, len(self.dados)):
                self.dicionario_grafo[self.dados[i][0]] = list()
                if len(self.dados[i]) == 3:
                    self.dicionario_grafo[self.dados[i][2]] = list()

            for i in range(0, len(self.dados)):
                if len(self.dados[i]) == 3:
                    if self.dados[i][2] not in self.dicionario_grafo[self.dados[i][0]]:
                        self.dicionario_grafo[self.dados[i][0]].append(self.dados[i][2])
                    if self.dados[i][0] not in self.dicionario_grafo[self.dados[i][2]]:
                        self.dicionario_grafo[self.dados[i][2]].append(self.dados[i][0])

        elif self.directed:
            print('direcionado')
            for i in range(0, len(self.dados)):
                self.dicionario_grafo[self.dados[i][0]] = list()
                if len(self.dados[i]) == 3:
                    self.dicionario_grafo[self.dados[i][2]] = list()
            for i in range(0, len(self.dados)):
                if len(self.dados[i]) == 3:
                    if self.dados[i][2] not in self.dicionario_grafo[self.dados[i][0]]:
                        self.dicionario_grafo[self.dados[i][0]].append(self.dados[i][2])

    # Complexidade de tempo: O(n)

    def mostrar_dicionario(self):
        for k, v in self.dicionario_grafo.items():
            print(f'{k}: {v}')


# Complexidade: O(n)

import os


class grafos:
    def __init__(self, dados=None, dicionario_grafo=None, vertices=None, directed=False):
        if dicionario_grafo is None:
            dicionario_grafo = {}
            dados = []
        self.dicionario_grafo = dicionario_grafo
        self.dados = dados
        self.vertices = vertices
        self.directed = directed

    def import_graph(self, nome_grafo):  # Complexidade de tempo: O(n)

        if os.path.isfile(nome_grafo):  # Verifica se o arquivo esá OK
            file = open(nome_grafo, 'r')
            for i in file.readlines():  # Itera por todas as linhas do arquivo
                graph = i.strip().split('  ')  # Da o split se contém 2 espaços
                self.dados.append(graph[0])
            file.close()
            if self.dados[0] == 'directed':
                self.directed = True
            elif self.dados[0] == 'undirected':
                self.directed = False
            else:
                print('Primeira linha do arquivo deve ser preenchida apenas com "directed" ou "undirected"')
                exit(1)
            del (self.dados[0])
            print(self.dados)

    def criar_dicionario(self):  # Complexidade de tempo: O(n)
        if not self.directed:
            print('Modo Não Direcionado')
            for i in range(0, len(self.dados)):
                self.dicionario_grafo[self.dados[i][0]] = list()
                self.dicionario_grafo[self.dados[i][2]] = list()
                if (self.dados[i][0], self.dados[i][2]) not in self.dados:
                    self.dados.append(self.dados[i][2] + ' ' + self.dados[i][0])

            for i in range(0, len(self.dados)):
                if self.dados[i][2] not in self.dicionario_grafo[self.dados[i][0]]:
                    self.dicionario_grafo[self.dados[i][0]].append(self.dados[i][2])
                if self.dados[i][2] not in self.dicionario_grafo[self.dados[i][0]]:
                    self.dicionario_grafo[self.dados[i][2]].append(self.dados[i][0])

        elif self.directed:
            print('Modo Direcionado')
            for i in range(0, len(self.dados)):
                self.dicionario_grafo[self.dados[i][0]] = list()
                self.dicionario_grafo[self.dados[i][2]] = list()

            for i in range(0, len(self.dados)):
                if self.dados[i][2] not in self.dicionario_grafo[self.dados[i][0]]:
                    self.dicionario_grafo[self.dados[i][0]].append(self.dados[i][2])

    def mostrar_grafo(self):
        for k, v in self.dicionario_grafo.items():
            print(f'{k}: {v}')

    def elementos_ordenados(self):
        lista_elementos = list()
        for i in range(0, len(self.dados)):
            if self.dados[i][0] not in lista_elementos:
                lista_elementos.append(self.dados[i][0])

            if self.dados[i][2] not in lista_elementos:  # and self.dados[i][2] != ' ':
                lista_elementos.append(self.dados[i][2])

        lista_elementos.sort()
        return lista_elementos

    def criar_matriz_adjacencia(self):
        ordenada = self.elementos_ordenados()

        if ' ' in ordenada:
            quant_vertice = len(ordenada) - 1
        else:
            quant_vertice = len(ordenada)
        self.matriz = [[0] * quant_vertice for i in range(quant_vertice)]  # criação da matriz que só tem zero

        for i in range(0, len(self.dados)):
            self.matriz[ordenada.index(self.dados[i][0])][ordenada.index(self.dados[i][2])] = 1
        for i in range(quant_vertice):
            print(self.matriz[i])

    # OK
    def inserir_vertice(self, vertice):
        self.vertices = vertice
        if self.vertices not in self.dicionario_grafo:
            key = self.vertices  # adiciona nova aresta
            self.dicionario_grafo[key] = list()
            self.dados.append(vertice + ' ' + ' ')
            print(f"\nO vertice '{self.vertices}' foi adicionado!!! \n")
        else:
            print(f"\nO vertice '{self.vertices}' já faz parte do grafo!!!\n")

    # OK para direcionado
    # OK para não direcionado
    def inserir_aresta(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

        if (self.v1 + ' ' + ' ') in self.dados:
            del self.dados[self.dados.index(self.v1 + ' ' + ' ')]
        v1_v2 = v1 + ' ' + v2
        v2_v1 = v2 + ' ' + v1

        if v1 and v2 in self.dicionario_grafo.keys():  # Verifica se as arestas existem antes de adicionar
            if self.directed:
                if v1_v2 not in self.dados:
                    self.dados.append(v1_v2)
                    self.dicionario_grafo[self.v1].append(self.v2)
                else:
                    print(f"A aresta {v1} --> {v2} já existe!!!")
            else:
                if v1_v2 not in self.dados:
                    self.dados.append(v1_v2)
                    self.dados.append(v2_v1)

                    self.dicionario_grafo[self.v1].append(self.v2)
                    self.dicionario_grafo[self.v2].append(self.v1)
                else:
                    print(f"A aresta {v1} <--> {v2} já existe!!!")
        else:
            if v1 not in self.dicionario_grafo.keys():
                print(f'{v1} Não é um vertice do grafo')
            elif v2 not in self.dicionario_grafo.keys():
                print(f'{v2} Não é um vertice do grafo')

    # OK direcionado
    # OK não direcionado
    def verifica_Aresta(self, v1, v2):
        self.criar_dicionario()
        self.v1 = v1
        self.v2 = v2

        if self.directed:
            if self.v1 in self.dicionario_grafo.keys():
                if self.v2 in self.dicionario_grafo[self.v1]:
                    print(f'A aresta {self.v1} -> {self.v2} existe')
                print(f'A aresta {self.v1} -> {self.v2} não existe')
        else:
            if self.v2 in self.dicionario_grafo[self.v1] and self.v1 in self.dicionario_grafo[self.v2]:
                print(f'A aresta {self.v1} -> {self.v2} existe')
            else:
                print(f'A aresta {self.v1} -> {self.v2} não existe')

    # OK
    def remover_vertice(self, vertice):
        if vertice in self.dicionario_grafo.keys():
            self.dicionario_grafo.pop(vertice)
            print(f"\nO vertice '{vertice}' foi removido.")

        else:
            if len(self.dicionario_grafo) == 0:
                print("\nNão há vertices para remoção :( ")
            else:
                print(f"\nNão hà vertice '{vertice}' para ser removido.")

        for k, v in self.dicionario_grafo.items():  # remoção geral da vertice(exclusão das arestas)
            if vertice in v:
                del v[v.index(vertice)]
        print(self.dicionario_grafo)

    # OK para direcionado
    # OK para não direcionado
    def remover_aresta(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

        print(self.dados)
        if self.directed:

            if (self.v1 + ' ' + self.v2) in self.dados:
                self.dados.remove(self.v1 + ' ' + self.v2)
                print(f"\nAresta '{self.v1 + ' ---> ' + self.v2}' removida")

            else:
                print(f"Não há aresta '{self.v1 + ' ---> ' + self.v2}' para ser removida")

        else:

            if (self.v1 + ' ' + self.v2) in self.dados:
                self.dados.remove(self.v1 + ' ' + self.v2)
                self.dados.remove(self.v2 + ' ' + self.v1)
                print(f"\nAresta '{self.v1 + ' --- ' + self.v2}' removida")

            else:
                print(f"\nNão há aresta '{self.v1 + ' --- ' + self.v2}' para ser removida")

        for k, v in self.dicionario_grafo.items():
            if self.directed:
                if k == self.v1:
                    if self.v2 in v:
                        del v[v.index(self.v2)]
                        pass
            else:
                if k == self.v1:
                    if self.v2 in v:
                        del v[v.index(self.v2)]
                if k == self.v2:
                    if self.v1 in v:
                        del v[v.index(self.v1)]
                        pass

    def verificar_vertices_adjacentes(self, vertice):
        vertices_adjacentes = list()
        ordenada = self.elementos_ordenados()
        tamanho = len(g.elementos_ordenados())
        posicao = ordenada.index(vertice)
        print(posicao)
        for i in range(0, tamanho):
            if self.matriz[posicao][i] == 1:
                vertices_adjacentes.append(ordenada[i])
            if self.matriz[i][posicao] == 1:
                vertices_adjacentes.append(ordenada[i])
        vertices_adjacentes = set(vertices_adjacentes)  # remove valores duplicados
        return vertices_adjacentes

    def verificar_vertices_incidentes(self, vertice):
        vertices_incidentes = list()
        ordenada = self.elementos_ordenados()
        tamanho = len(g.elementos_ordenados())
        posicao = ordenada.index(vertice)
        for i in range(0, tamanho):
            if self.matriz[i][posicao] == 1:
                vertices_incidentes.append(ordenada[i])

        return vertices_incidentes

    def grafo_complemento(self, base):
        tamanho = len(g.elementos_ordenados())
        self.matriz = [[0] * tamanho for i in range(tamanho)]
        for i in range(0, tamanho):
            for j in range(0, tamanho):
                if base.matriz[i][j] == 1:
                    self.matriz[i][j] = 0
                else:
                    self.matriz[i][j] = 1
        for i in range(tamanho):
            print(self.matriz[i])

    def grafo_transposto(self, base):
        tamanho = len(g.elementos_ordenados())
        self.matriz = [[0] * tamanho for i in range(tamanho)]
        for i in range(0, tamanho):
            for j in range(0, tamanho):
                if base.matriz[i][j] == 1:
                    self.matriz[j][i] = 1
                else:
                    self.matriz[j][i] = 0
        for i in range(tamanho):
            print(self.matriz[i])


g = grafos()
k = grafos()
g.import_graph('grafo.txt')
g.criar_matriz_adjacencia()
g.criar_dicionario()

print('')
g.mostrar_grafo()
print(g.verificar_vertices_incidentes('b'))

k.grafo_transposto(g)









