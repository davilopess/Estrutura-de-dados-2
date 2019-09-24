from grafo import Grafo
from algoritmosDeOrdenacao import *
from utils import *
import argparse
import time
import json

'''
Implemente o algoritmo de ordenação no arquivo algoritmosDeOrdenacao.py
Instruções básicas de como fazer a implementação estão no arquivo algoritmosDeOrdenacao.py
'''
parser = argparse.ArgumentParser()

parser.add_argument('--archive', type = str, dest = 'arch', required = True, help = 'Endereco do arquivo para ser ordenado')
parser.add_argument('--save', type=str,dest='save',  help='Endereco para salvar o arquivo')
parser.add_argument('--operations', type = str, dest='op', help = 'Escolha a operacao de ordenacao')

args = parser.parse_args()
if __name__ == "__main__":


    if  args.op == 'insert':
        algoritimoDeOrdenacao = InsertionSort()

    elif args.op == 'selection':
        algoritimoDeOrdenacao = SelectionSort()
        print("selection")
    elif args.op == 'shell':
        algoritimoDeOrdenacao = ShellSort()
    elif args.op == 'merge':
        algoritimoDeOrdenacao = MergeSort()
    inicio = time.time()
    arquivoJson = args.arch
    arquivoDeSaida = args.save

    grafo = Grafo()
    grafo.estabelecerAlgoritmoDeOrdencao(algoritimoDeOrdenacao)
    grafo.carregarGrafo(arquivoJson)

    arvoreGeradoraMinima =  grafo.executarKruskal()
    SalvarArvoreGeradoraMinimaEmArquivo(arquivoDeSaida, arvoreGeradoraMinima)
    fim = time.time()
    print("TEMPO DE EXECUÇÃO : {}".format(fim - inicio))
