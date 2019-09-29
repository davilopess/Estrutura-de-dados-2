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
parser.add_argument('--operations', type = str, dest='op', help = 'Escolha a operacao de ordenaca[insert, selection, shell, mergep, mergef, quick]')
parser.add_argument('--L', dest='L', help='Escolha o L')


args = parser.parse_args()
if __name__ == "__main__":

                                                                                                #A operacao escolhida pelo usuario entra no if respectivo
    if  args.op == 'insert':
        algoritimoDeOrdenacao = InsertionSort()

    elif args.op == 'selection':
        algoritimoDeOrdenacao = SelectionSort()

    elif args.op == 'shell':
        algoritimoDeOrdenacao = ShellSort()
    elif args.op == 'mergep':

        algoritimoDeOrdenacao = MergeSortInicial()
    elif args.op == 'mergef':
        algoritimoDeOrdenacao = MergeSortFinal()

    elif args.op == 'quick':
        algoritimoDeOrdenacao = QuickSort()

    inicio = time.time()
    arquivoJson = args.arch
    arquivoDeSaida = args.save

    grafo = Grafo()
    if args.op == 'merge':                                                                     #Se o merge for escolhido é preciso passar o L como parametro
        grafo.estabelecerAlgoritmoDeOrdencao(algoritimoDeOrdenacao, args.L)
    elif args.op == 'quick':
        grafo.estabelecerAlgoritmoDeOrdencao(algoritimoDeOrdenacao, 0, args.L)                 #O zero é um parametro que serve apenas para diferenciar do merge
    else:
        grafo.estabelecerAlgoritmoDeOrdencao(algoritimoDeOrdenacao, args.L)

    grafo.carregarGrafo(arquivoJson)
    arvoreGeradoraMinima =  grafo.executarKruskal()
    SalvarArvoreGeradoraMinimaEmArquivo(arquivoDeSaida, arvoreGeradoraMinima)
    fim = time.time()
    print("TEMPO DE EXECUÇÃO : {}".format(fim - inicio))
