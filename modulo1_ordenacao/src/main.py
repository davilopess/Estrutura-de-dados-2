from grafo import Grafo
from algoritmosDeOrdenacao import *
from utils import *
import argparse
import json

'''
Implemente o algoritmo de ordenação no arquivo algoritmosDeOrdenacao.py
Instruções básicas de como fazer a implementação estão no arquivo algoritmosDeOrdenacao.py
'''

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--archive', type = str, dest = 'arch', required = True, help = 'Endereco do arquivo para ser ordenado')
    parser.add_argument('--save', type=str,dest='save',  help='Endereco para salvar o arquivo')
    parser.add_argument('--operations', type = str, help = 'Escolha a operacao de ordenacao')

    args = parser.parse_args()

    if  args.operations == 'insert':
        algoritimoDeOrdenacao = InsertionSort()

    elif args.operations == 'selection':
        algoritimoDeOrdenacao = SelectionSort()

    elif args.operations == 'shell':
        algoritimoDeOrdenacao = SelectionSort()

    arquivoJson = args.arch
    arquivoDeSaida = args.save

    grafo = Grafo()
    grafo.estabelecerAlgoritmoDeOrdencao
    grafo.carregarGrafo(arquivoJson)

    arvoreGeradoraMinima =  grafo.executarKruskal()
    SalvarArvoreGeradoraMinimaEmArquivo(arquivoDeSaida, arvoreGeradoraMinima)

