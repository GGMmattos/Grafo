#Gabriel Gonçalves de Matos
#Rafael Prado Torres

import os
class grafos:
    def __init__(self, dados=None, lista_adjacencia=None, vertices=None, directed=False, quant_vertice=None, lista_complemento=None):
        self.v2 = None
        self.v1 = None
        if lista_adjacencia is None:
            lista_adjacencia = {}
            dados = []

        self.lista_complemento = lista_complemento
        self.lista_adjacencia = lista_adjacencia
        self.dados = dados
        self.vertices = vertices
        self.directed = directed
        self.quant_vertice = quant_vertice

    #Complexidade: Theta(n) | n = nº de linhas do arquivo lido
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

    #Complexidade: Theta(n) | n = tamanho de dados
    def criar_dicionario(self):  # Complexidade de tempo: O(n)
        if not self.directed:
            print('Modo Não Direcionado')
            for i in range(0, len(self.dados)): #UTILIZADO DICIONÁRIOS COM LISTAS -
                self.lista_adjacencia[self.dados[i][0]] = list()    #ATRIBUIÇÃO AOS ELEMENTOS NA LISTA
                self.lista_adjacencia[self.dados[i][2]] = list()
                if (self.dados[i][0], self.dados[i][2]) not in self.dados:
                    self.dados.append(self.dados[i][2] + ' ' + self.dados[i][0]) #PARA GRAFO NÃO ORIENTADO É CRIADA A RESTA INVERSA

            for i in range(0, len(self.dados)):
                if self.dados[i][2] not in self.lista_adjacencia[self.dados[i][0]]: #Se V2 já está na lista de V1(é adjacente)
                    self.lista_adjacencia[self.dados[i][0]].append(self.dados[i][2]) #Caso não esteja o V2 é adicionado a lista de V1
                if self.dados[i][0] not in self.lista_adjacencia[self.dados[i][2]]: #Se V1 já está na lista de V2(é adjacente)
                    self.lista_adjacencia[self.dados[i][2]].append(self.dados[i][0]) #Caso não esteja o V2 é adicionado a lista de V1

        #Complexidade: Theta(n) | n = tamanho de dados
        elif self.directed:
            print('Modo Direcionado')
            for i in range(0, len(self.dados)):
                self.lista_adjacencia[self.dados[i][0]] = list()
                self.lista_adjacencia[self.dados[i][2]] = list()

            for i in range(0, len(self.dados)):
                if self.dados[i][2] not in self.lista_adjacencia[self.dados[i][0]]:#Se V2 já está na lista de V1(é adjacente)
                    self.lista_adjacencia[self.dados[i][0]].append(self.dados[i][2]) #Caso não esteja o V2 é adicionado a lista de V1

    #Complexidade: Theta(n) | n = tamanho de dados
    def elementos_ordenados(self): #Ordenação dos elementos
        lista_elementos = list()
        for i in range(0, len(self.dados)):
            if self.dados[i][0] not in lista_elementos:
                lista_elementos.append(self.dados[i][0])
                lista_elementos.append(self.dados[i][2])
        lista_elementos.sort()
        return lista_elementos

    #Complexidade: Theta(1)
    def inserir_vertice(self, vertice):
        self.vertices = vertice
        if self.vertices not in self.lista_adjacencia:
            key = self.vertices
            self.lista_adjacencia[key] = list() #Adiciona o novo vertie como chave do dicionário
            self.dados.append(vertice + ' ' + ' ') #A principio o vertice é adicionado sem adjacentes
            print(f"\nO vertice '{self.vertices}' foi adicionado!!! \n")
        else:
            print(f"\nO vertice '{self.vertices}' já faz parte do grafo!!!\n")

    #Complexidade: Theta(1)
    def inserir_aresta(self, v1, v2):
        v1 = v1
        v2 = v2

        if (v1 + ' ' + ' ') in self.dados:
            del self.dados[self.dados.index(v1 + ' ' + ' ')] #Tratamento caso V1 não contenha adjacentes até aqui
        v1_v2 = v1 + ' ' + v2 #Concatenação para o formato da lista(par de vertices)
        v2_v1 = v2 + ' ' + v1

        if v1 and v2 in self.lista_adjacencia.keys():  # Verifica se as arestas existem antes de adicionar
            if self.directed:
                if v1_v2 not in self.dados:
                    self.dados.append(v1_v2) #Adiciona na lista
                    self.lista_adjacencia[v1].append(v2) #Adiciona no dicionário (lista de adjacencia)
                else:
                    print(f"\nA aresta {v1} --> {v2} já existe!!!")
            else:
                if v1_v2 not in self.dados:
                    self.dados.append(v1_v2) #Adiciona aresta à lista
                    self.dados.append(v2_v1)

                    self.lista_adjacencia[self.v1].append(v2)#Adiciona aresta ao dicionário
                    self.lista_adjacencia[self.v2].append(v1)
                else:
                    print(f"\nA aresta {v1} <--> {v2} já existe!!!")
        else:
            if v1 not in self.lista_adjacencia.keys():
                print(f'\n{v1} Não é um vertice do grafo')
            elif v2 not in self.lista_adjacencia.keys():
                print(f'\n{v2} Não é um vertice do grafo')

    #Complexidade: Theta(n) | n = tamanho da lista de adjacencia
    def remover_vertice(self, vertice):
        if vertice in self.lista_adjacencia.keys():
            self.lista_adjacencia.pop(vertice)
            print(f"\nO vertice '{vertice}' foi removido\n")

        else:
            if len(self.lista_adjacencia) == 0:
                print("\nNão há vertices para remoção\n")
            else:
                print(f"\nNão hà vertice '{vertice}' no grafo para ser removido.\n")

        for k, v in self.lista_adjacencia.items():  # remoção geral da vertice(exclusão das arestas)
            if vertice in v:
                del v[v.index(vertice)]

    #Complexidade: Theta(n) | n = tamanho da lista de adjacencia
    def remover_aresta(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

        if self.directed:

            if (self.v1 + ' ' + self.v2) in self.dados:
                self.dados.remove(self.v1 + ' ' + self.v2)
                print(f"\nAresta '{self.v1 + ' ---> ' + self.v2}' removida\n")

            else:
                print(f"\nNão há aresta '{self.v1 + ' ---> ' + self.v2}' para ser removida\n")

        else:

            if (self.v1 + ' ' + self.v2) in self.dados:
                self.dados.remove(self.v1 + ' ' + self.v2)
                self.dados.remove(self.v2 + ' ' + self.v1)
                print(f"\nAresta '{self.v1 + ' --- ' + self.v2}' removida\n")

            else:
                print(f"\nNão há aresta '{self.v1 + ' --- ' + self.v2}' para ser removida\n")

        for k, v in self.lista_adjacencia.items():
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

    #Complexidade: Theta(n) | n = tamanho da lista de adjacencia
    def mostrar_grafo(self):
        for k, v in self.lista_adjacencia.items():
            print(f'{k}: {v}')

    #Complexidade: Theta(n)
    def matriz_adjacencia(self):
        ordenada = self.elementos_ordenados()

        if ' ' in ordenada:
            self.quant_vertice = len(ordenada) - 1
        else:
            self.quant_vertice = len(ordenada)
        self.matriz = [[0] *  self.quant_vertice for i in range(self.quant_vertice)]  # criação da matriz que só tem zero

        for i in range(0, len(self.dados)):
            x = ordenada.index(self.dados[i][0])
            y = ordenada.index(self.dados[i][2])
            self.matriz[x][y] = 1
            #insere 1 conforme as posições x e y (com base nos dados)

        print('\n\nMatriz de adjacência\n')
        for i in range(self.quant_vertice):
            print(self.matriz[i])

    #Complexidade: Theta(1)
    def verifica_aresta(self, v1, v2):
        self.criar_dicionario()
        self.v1 = v1
        self.v2 = v2

        if self.directed:
            if self.v1 in self.lista_adjacencia.keys():
                if self.v2 in self.lista_adjacencia[self.v1]:
                    print(f'A aresta {self.v1} -> {self.v2} existe')
                print(f'A aresta {self.v1} -> {self.v2} não existe')
        else:
            if self.v2 in self.lista_adjacencia[self.v1] and self.v1 in self.lista_adjacencia[self.v2]:
                print(f'A aresta {self.v1} -> {self.v2} existe')
            else:
                print(f'A aresta {self.v1} -> {self.v2} não existe')

    # #Complexidade: Theta(n)
    # def verificar_vertices_adjacentes(self, vertice):
    #     vertices_adjacentes = list()
    #     ordenada = self.elementos_ordenados()
    #     tamanho = len(g.elementos_ordenados())
    #     posicao = ordenada.index(vertice)
    #     for i in range(0, tamanho): #Lê a linha e coluna
    #         if self.matriz[posicao][i] == 1:
    #             vertices_adjacentes.append(ordenada[i])
    #         if self.matriz[i][posicao] == 1:
    #             vertices_adjacentes.append(ordenada[i])
    #             #A matriz é ordenada em ordem alfabetica, o que justifica essa operação
    #     vertices_adjacentes = set(vertices_adjacentes)  # remove valores duplicados7
    #
    #     return print(f'\nVertice(s) adjacente de {vertice}: {vertices_adjacentes}\n')

    def verifica_adjacentes(self, vertice): #O(1)
        print(f'\nO(s) adjacente(s) de {vertice}: {self.lista_adjacencia[vertice]}\n')

    #Complexidade: Theta(n)
    def verificar_vertices_incidentes(self, vertice): #Vertice deve ser string
        vertices_incidentes = list()
        ordenada = self.elementos_ordenados()
        tamanho = len(g.elementos_ordenados())
        posicao = ordenada.index(vertice)
        for i in range(0, tamanho): #Lê a coluna, para ver os vértices que incidiram em vértice
            if self.matriz[i][posicao] == 1:
                vertices_incidentes.append(ordenada[i])

        return print(f'\nVertice(s) incidente de {vertice}: {vertices_incidentes}\n')


    #Complexidade: Theta(n²)
    def grafo_complemento(self, base):#Lê a matriz de um grafo e coloca em outro #foi excluido o argumento base

        tamanho = len(g.elementos_ordenados())
        self.matriz = [[0] * tamanho for i in range(tamanho)]
        for i in range(0, tamanho): #O que é linha vira coluna, e vice-versa
            for j in range(0, tamanho):
                if base.matriz[i][j] == 1:
                    self.matriz[i][j] = 0
                else:
                    self.matriz[i][j] = 1
        for i in range(tamanho):
            print(self.matriz[i])

    #Complexidade: Theta(n²)
    def grafo_transposto(self, base): #Lê a matriz de um grafo e coloca em outro
        tamanho = len(g.elementos_ordenados())
        self.matriz = [[0] * tamanho for i in range(tamanho)]
        for i in range(0, tamanho): #Transforma o que é 1 em 0, e vice-versa
            for j in range(0, tamanho):
                if base.matriz[i][j] == 1:
                    self.matriz[j][i] = 1
                else:
                    self.matriz[j][i] = 0
        for i in range(tamanho):
            print(self.matriz[i])


g = grafos()
g.import_graph('grafo.txt') #
g.criar_dicionario()
# g.matriz_adjacencia()
# k = grafos()
# g.verifica_adjacentes('a')
