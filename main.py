import os


class grafos:
    def __init__(self, dados=None, dicionario_grafo=None, vertices=None, directed=False, teste=None, modo=None): 
        if dicionario_grafo is None:
            dicionario_grafo = {}
            dados = []
        self.dicionario_grafo = dicionario_grafo
        self.dados = dados
        self.teste = teste
        self.vertices = vertices
        self.directed = directed
        self.modo = modo

    def import_graph(self, nome_grafo):
        if os.path.isfile(nome_grafo):  # Verifica se o arquivo esá OK
            file = open(nome_grafo, 'r')
            for i in file.readlines():  # Itera por todas as linhas do arquivo
                graph = i.strip().split('  ')  # Da o split se contém 2 espaços
                self.dados.append(graph[0])
            file.close()
            self.modo = self.dados[0]
            del (self.dados[0])

    def criar_dicionario(self):
        if self.modo == 'undirected':
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

        elif self.modo == 'directed':
            self.directed = True
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
            if self.dados[i][2] not in lista_elementos:
                lista_elementos.append(self.dados[i][2])
        lista_elementos.sort()
        return lista_elementos

    def criar_matriz_adjacencia(self):
        ordenada = self.elementos_ordenados()
        self.Quant_vertice = len(ordenada)
        self.matriz = [[0] * self.Quant_vertice for i in range(self.Quant_vertice)]  # criação da matriz que só tem zero

        dados = self.dados

        for i in range(0, len(dados)):
            # self.matriz[0][2] = 1
            # self.matriz[ordenada.index('a')][ordenada.index('c')] = 1
            self.matriz[ordenada.index(dados[i][0])][ordenada.index(dados[i][2])] = 1
        for i in range(self.Quant_vertice):
            print(self.matriz[i])

    #OK
    def inserir_vertice(self, vertice):
        self.vertices = vertice
        if self.vertices not in self.dicionario_grafo:
            key = self.vertices  # adiciona nova aresta
            self.dicionario_grafo[key] = list()
            self.dados.append(vertice+' '+' ')
            print(f"O vertice '{self.vertices}' foi adicionado!!! ")
        else:
            print(f"O vertice '{self.vertices}' já faz parte do grafo!!!")

    #OK para direcionado
    #OK para não direcionado
    def inserir_aresta(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

        print(self.dados)
        if (self.v1+' '+' ') in self.dados:
            del self.dados[self.dados.index(self.v1+' '+' ')]
        v1_v2 = v1+' '+v2
        v2_v1 = v2+' '+v1

        print(self.dados)
        print('')
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

    #OK direcionado
    #OK não direcionado
    def verifica_Aresta(self, v1, v2):
        self.criar_dicionario()
        self.v1 = v1
        self.v2 = v2

        if self.directed:
            if self.v2 in self.dicionario_grafo[self.v1]:
                print(f'A aresta {self.v1} -> {self.v2} existe')
            else:
                print(f'A aresta {self.v1} -> {self.v2} não existe')
        else:
            if self.v2 in self.dicionario_grafo[self.v1] and self.v1 in self.dicionario_grafo[self.v2]:
                print(f'A aresta {self.v1} -> {self.v2} existe')
            else:
                print(f'A aresta {self.v1} -> {self.v2} não existe')

    #OK
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

    #OK para direcionado
    #OK para não direcionado
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



g = grafos()
g.import_graph('grafo.txt')
g.criar_dicionario()

g.mostrar_grafo()
print('')

g.inserir_vertice('z')
g.inserir_vertice('k')
g.inserir_aresta('z', 'a')
g.inserir_aresta('k', 'c')
g.inserir_aresta('a', 'k')
g.verifica_Aresta('a','z')
g.mostrar_grafo()







