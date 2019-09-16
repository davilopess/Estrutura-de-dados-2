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





class InsertionSort(object):
    def ordenar(self, colecao):
        '''
        O método ordenar recebe uma colecão
        realiza ordenacão na colecão
        retorna colecão após ordenação
        '''
        for j in range(1,len(colecao)):
            chave = colecao[j]

            i = j - 1;
            while i>= 0 and int(colecao[i]['weight'])  > int(chave['weight']) :
                colecao[i + 1] = colecao[i]
                i = i - 1

            colecao[i+1] = chave

        return colecao

class SelectionSort(object):
    def ordenar(self, colecao):
        for i in range(0, len(colecao)-1):
            min = i
            for j in range(i+1, len(colecao)):
                if (int(colecao[j]['weight']) < int(colecao[min]['weight'])):
                    min = colecao[j]

                    colecao[min], colecao[i] = colecao[i], colecao[m]

        return colecao

class ShellSort(object):
    def ordenar(self,colecao):
        h = 1
        for h in range(1, len(colecao), h = (3*h)+1):


            while ( h > 0 ):
                h = ( (h - 1) / 3)

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
    def ordenar(self, colecao):
'''







