'''
Introdução:
- Implementar algoritmo de ordenação que receba uma colecão
- A coleção é uma lista de arestas
- Para comparar o peso as arestas entre dois item da coleção basta usar a chave 'weight' (peso)

Exemplos:
- Modo convencional
colecao[i] operador de comparacao colecao[j]
colecao[i] < colecao[j]

- Modo que você vai usar
int(colecao[i]['weight']) operador de comparacao int(colecao[j]['weight'])
int(colecao[i]['weight']) < int(colecao[j]['weight'])

É nescessário converter o valor pra Interger no momento da comparação a fim de evitar erros
'''


# Sua classe algoritmo de ordenação precisar ter um método ordenar
import time
import sys
sys.setrecursionlimit(1000000000)                                                                      #aumenta o limite de recursividade


class InsertionSort(object):
    def ordenar(self, colecao):
        '''
        O método ordenar recebe uma colecão
        realiza ordenacão na colecão
        retorna colecão após ordenação
        '''

        for j in range(1,len(colecao)):
            chave = colecao[j]                                                                      #Elege uma chave do vetor para ser comparada
            i = j - 1;                                                                              #O indice é a chave antes do eleito
            while i>= 0 and int(colecao[i]['weight'])  > int(chave['weight']):                      #Enquanto existir chaves antes do eleito ele é comparado
                colecao[i + 1] = colecao[i]
                i = i - 1

            colecao[i+1] = chave
        return colecao

class SelectionSort(object):
    def ordenar(self, colecao):
        for i in range(0, len(colecao) - 1):
            min = i                                                                                 #Primeira chave da colecao é eleita a minima
            for j in range(i+1, len(colecao)):                                                      #Compara até achar uma chave menor
                if (int(colecao[j]['weight']) < int(colecao[min]['weight'])):
                    min = j

            colecao[min], colecao[i] = colecao[i], colecao[min]
        return colecao

class ShellSort(object):
    def ordenar(self,colecao):
        h = 1
        for h in range(1, len(colecao), (3*h)+1):                                                   #calcula o h
            while ( h > 0 ):
                h = int( (h - 1) / 3)                                                               #Atualiza o valor do h

                for i in range(h, len(colecao)):
                    aux = colecao[i]
                    j = i

                    while int(colecao[j-h]['weight']) > int(aux['weight']):
                        colecao[j] = colecao[j-h]
                        j = j - h

                        if (j < h):
                            break
                    colecao[j] = aux
        return colecao
'''
class MergeSort(object):
    def merge(self, colecao,first,  mid, last):
        left = colecao[first:mid]
        right = colecao[mid:last + 1]

        i = j = 0

        for k in range (first, last + 1):
            if int(left[i]['weight']) <= int(right[j]['weight']):
                colecao[k] = left[i]
                i+=1
            else:
                colecao[k] = right[j]
                j += 1
    def mergesort(self, colecao, first, last):
        if first < last:
            mid = (first + last)//2
            self.mergesort(colecao, first, mid)
            self.mergesort(colecao, mid + 1, last)
            self.merge(colecao, first, mid, last)

    def ordenar(self, colecao):
        return self.mergesort( colecao, 0, len(colecao) - 1)
'''

class MergeSortInicial(object):

    def ordenar(self, colecao, L):
        cont = 0

        mid = int(len(colecao)/2)                                                                   #encontra o meio da colecao

        left = colecao[:mid]                                                                        #Pega a lista da esquerda
        right = colecao[mid:]                                                                       #Pega a lista da direita
        cont = cont + 1
        if len(left)<= int(L) and len(right)<= int(L):                                              #Compara se o L é igual ou maior que as listas
                                                                                                    #Se for, as listas sao ordenadas independentemente por inserção
            algorit = InsertionSort()

            algorit.ordenar(left)
            algorit.ordenar(right)

        elif len(colecao) > 1:                                                                      #Se nao for, a lista continua se dividindo

            self.ordenar(left, L)
            self.ordenar(right, L)

        i = j = k = 0                                                                               #
        cont = cont + 1
        while i < len(left) and j < len(right):                                                     #As listas voltam sendo mescladas
            cont = cont + 1
            if int(left[i]['weight']) < int(right[j]['weight']):
                cont = cont + 1
                colecao[k] = left[i]
                i+=1
            else:
                colecao[k] = right[j]
                j+=1
            k+=1
        cont = cont + 1
        while i < len(left):

            colecao[k] = left[i]
            i += 1
            k += 1
        cont = cont + 1
        while j < len(right):

            colecao[k] = right[j]
            j += 1
            k += 1
        print(cont)
        return colecao

class MergeSortFinal(object):

    def ordenar(self, colecao, L):
        cont = 0
        mid = int(len(colecao)/2)

        left = colecao[:mid]
        right = colecao[mid:]
        cont = cont + 1
        if len(colecao) > 1 or len(left)>= int(L) or len(right)>= int(L):                            #Se o L for menor ou igual as listas o algoritmo continua dividindo
            self.ordenar(left, L)
            self.ordenar(right, L)

        i = j = k = 0
        cont = cont + 1
        while i < len(left) and j < len(right):                                                      # Quando o L é maior a divisao para e as listas sao mescladas
            cont = cont + 1
            if int(left[i]['weight']) < int(right[j]['weight']):
                colecao[k] = left[i]
                i+=1
            else:
                colecao[k] = right[j]
                j+=1
            k+=1

        algorit = InsertionSort()

        algorit.ordenar(colecao)
        '''
        while i < len(left):
            colecao[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            colecao[k] = right[j]
            j += 1
            k += 1
        '''
        print(cont)
        return colecao


class QuickSort(object):
    def ordenar(self, colecao, inicio, fim, L):

        if inicio < fim:

            posiPivo = self.particiona(colecao, inicio, fim)



            self.ordenar(colecao, inicio, posiPivo - 1, L)
            self.ordenar(colecao, posiPivo + 1, fim, L)


        return colecao
    def particiona(self, colecao, inicio, fim):

        pivo = colecao[inicio]
        i = inicio + 1
        f= fim

        while (i <= f):

            if int(colecao[i]['weight']) <= int(pivo['weight']):
                i+=1
            elif int(pivo['weight']) < int(colecao[f]['weight']):
                f-=1
            else:
                colecao[i], colecao[f] = colecao[f], colecao[i]

        colecao[inicio] = colecao[f]
        colecao[f] = pivo

        return f