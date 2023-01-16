class Grafos:

    def __init__(self, vertices): #definindo inicio da classe, sendo vertcice o númeor de vertices
        self.vertices = vertices #recebe a quantidade de vertices
        self.grafos = [[0] * self.vertices for i in  range(self.vertices)] #criação da matriz que só tem zero

    def adiciona_arestas(self, u , v): #arestas U e V
        #pensando em grafos direcionados simples
        self.grafos[u-1][v-1] = 1 #tiramos 1 porque python começa a contagem do zero..
        #OBS para gráficos multiplos trocamos = para +=

        #Mas e se não for grafos direcionados?
        # def adiciona_arestas(self, u, v):
        #     self.grafos[u - 1][v - 1] = 1
        #     self.grafos[v - 1][u - 1] = 1


    def mostra_matriz(self):
        print('A matriz de adjacencias é: ')
        for i in range(self.vertices):
            print(self.grafos[i])

g = Grafos(12)

g.adiciona_arestas(1,2)
g.adiciona_arestas(3,4)
g.adiciona_arestas(2,3)

g.mostra_matriz()
