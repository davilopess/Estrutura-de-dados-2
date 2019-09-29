import json
import copy


class Grafo(object):
    def __init__(self):
        self.algoritimoDeOrdenacao = None
        self.vertices = None
        self.arestas = None
        self.possui = None
        return

    def _algortmoDeOrdencaoErro(self):
        if self.algoritimoDeOrdenacao is None:
            print('Algoritmo de Ordencação Nulo, finalizando programa.')
            raise ValueError

    def estabelecerAlgoritmoDeOrdencao(self, algoritimoDeOrdenacao, possui = None, possui2 = None):
        self.algoritimoDeOrdenacao = algoritimoDeOrdenacao
        self.possui = possui
        self.possui2 = possui2
    def executarKruskal(self):
        self._algortmoDeOrdencaoErro()
        return self._kruskal()

    def _conectaDuasArvoresDiferentes(self, floresta, aresta):
        for arvore in floresta:
            if aresta['source'] in arvore and aresta['target'] in arvore:
                return False
        return True

    def _concatenaArvores(self, floresta, aresta):
        arvoreA = None
        arvoreB = None
        for arvore in floresta:
            if(aresta['source'] in arvore):
                arvoreA = arvore
            if(aresta['target'] in arvore):
                arvoreB = arvore
        if arvoreA is not None and arvoreB is not None:
            if arvoreA != arvoreB:
                novaArvore = arvoreA + arvoreB
                floresta.remove(arvoreA)
                floresta.remove(arvoreB)
                floresta.append(novaArvore)

    def _kruskal(self):
        print('Executando kruskal, aguarde...')
        floresta =  [ [vertice['id'] ] for vertice in self.vertices]
        arvoreGeradoraMinima = []

        # Ordencão das arestas iniciada
        if self.possui2 != None:
            arestasOrdenadas = self.algoritimoDeOrdenacao.ordenar(copy.copy(self.arestas),0, len(self.arestas)-1 , self.possui2)                            #Se for selecionado o quick os parametros aumentam

        elif self.possui != None:
            arestasOrdenadas = self.algoritimoDeOrdenacao.ordenar( copy.copy(self.arestas), self.possui )                                                   #Se for selecionado o merge é preciso passar o L

        else:
            arestasOrdenadas = self.algoritimoDeOrdenacao.ordenar(copy.copy(self.arestas))



        # Ordencão das arestas finalizada

        pop = 0
        while len(arestasOrdenadas) > pop:
            aresta = arestasOrdenadas[pop]
            pop+=1
            if(self._conectaDuasArvoresDiferentes(floresta, aresta)):
                arvoreGeradoraMinima.append(aresta)
                self._concatenaArvores(floresta, aresta)
        return arvoreGeradoraMinima

    def carregarGrafo(self, arquivoJson):
        print('Carregando grafo, aguarde...')
        with open(arquivoJson) as arquivo:
            grafo_json = json.loads(arquivo.read())
            self.vertices = grafo_json['graph']['nodes']
            self.arestas = grafo_json['graph']['edges']
        return True