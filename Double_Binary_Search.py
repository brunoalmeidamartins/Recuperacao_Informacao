'''
Verifica se um conjunto possui mais elementos que o outro subset(D) > subset(Q)
'''
def ComparaConjuntos(D,Q,inicioD, fimD, inicioQ, fimQ):
    result = True
    vet_aux1 = []
    vet_aux2 = []
    #Inverte os indices caso os valores sejam negativos
    if inicioD > fimD:
        aux = inicioD
        inicioD = fimD
        fimD = aux
    if inicioQ > fimQ:
        aux = inicioQ
        inicioQ = fimQ
        fimQ = aux
    for i in range(inicioD, fimD):
        vet_aux1.append(D[i])
    for i in range(inicioQ, fimQ):
        vet_aux2.append(Q[i])
    if len(vet_aux1) > len(vet_aux2):
        result = True
    else:
        result = False
    return [result, vet_aux1, vet_aux2]

'''
Funcao de busca binaria
'''
def BinSearch(chave, D, minD, maxD): #Retorna posicao
    #Condicao de parada da recursao
    if minD <= maxD:
        q = (minD + maxD) // 2
        if chave > D[q]:
            return BinSearch(chave, D, q+1, maxD)
        elif chave < D[q]:
            return BinSearch(chave, D, minD, q - 1)
        else:
            return [q, chave] #Retorna a posicao e valor ## Achou o valor midQval
    #Elemento nao encontrado no vetor
    if maxD+1 < len(D):
        return [maxD+1, -1] #Retorna a posicao mais alta depois do valor a ser encontrado \  ex: 5 entre 4 e 6; retorna a posicao do 6
    else:
        return [maxD, -1]


'''
Funcao de Interseccao de duas listas ordenadas
'''
def Intersect(D, Q, minD, maxD, minQ, maxQ, result):
    if len(Q) == 0 or len(D) == 0: #Se alguma das listas for vazia, entao termina recursao e retorna o vetor vazio!!
        return []
    #Condicacao de parada da recursao
    print("")
    print("Condicao de parada:", minD," > ", maxD, " or", minQ, " > ", maxQ)
    if minD > maxD or minQ > maxQ:
        print("Para recursao")
        return
    midQ = (minQ+maxQ) // 2 #Pega a posicao do elemento do meio do vetor Q
    midQval = Q[midQ] #Pega o valor do elemento do meio
    busca_binaria = BinSearch(midQval, D, minD, maxD) # Faz a busca binaria do elemento de Q no vetor D
    midD = busca_binaria[0] #Recebe a posicao do valor no Vetor D ou a proxima posicao se o elemento nao for encontrado
    print("Valores:")
    print("midQ = ", midQ)
    print("midQval = ", midQval)
    print("midD = ", midD)
    '''
    Primeiro IF verifica se o subconjunto (D) > subconjunto (Q)
    Essa comparacacao eh feita pegando o maior elemento do subconjunto (D) e comparando com o maior elemento do subconjunto (Q)
    Caso nao seja, a logica da procura eh invertida
    '''
    print("")
    result_comparacao = ComparaConjuntos(D,Q,minD, midD-1, minQ, midQ-1)
    #result_comparacao = ComparaConjuntos(D,Q,minD, midD, minQ, midQ)
    print('1. Compara os tamanhos dos conjuntos:  %d > %d' % (len(result_comparacao[1]),len(result_comparacao[2])))
    if result_comparacao[0]:
        print("Mantem a busca na lista D!")
        print('1.1 - Intersect(D, Q, %d, %d, %d, %d)' %( minD,midD - 1, minQ, midQ - 1))
        Intersect(D, Q, minD,midD - 1, minQ, midQ - 1, result)
        print("")
    else:
        print("Inverte a busca! Busca na lista Q!")
        print('1.2 - Intersect(Q, D, %d, %d, %d, %d)' % (minQ, midQ - 1, minD, midD - 1))
        Intersect(Q, D, minQ, midQ - 1, minD, midD - 1, result)
        print("")

    '''
    Segundo IF verifica se o valor encontrado no vetor D eh o mesmo de do vetor Q
    Se sim, entao adiciona o valor a resposta, pois corresponde a uma interseccao 
    '''
    print("")
    print("Valor de midD: ", midD)
    print('2 - D[midD]:%d == midQval:%d ' % (D[midD], midQval))
    if D[midD] == midQval:
        print("2.1 - Adicionando o resultado no vetor result")
        result.append(midQval)
        midD = midD - 1
        print("")

    '''
    Terceiro IF verifica se o subconjunto (D) > subconjunto (Q)
    Essa comparacacao eh feita pegando o maior elemento do subconjunto (D) e comparando com o menor elemento do subconjunto (Q)
    Caso nao seja, a logica da procura eh invertida
    '''
    print("")
    result_comparacao = ComparaConjuntos(D, Q, midD+1,maxD,midQ+1,maxQ)
    #result_comparacao = ComparaConjuntos(D, Q, midD,maxD,midQ,maxQ)
    print('3. Compara os tamanhos dos conjuntos: %d > %d' % (len(result_comparacao[1]), len(result_comparacao[2])))
    if result_comparacao[0]:
        print("Mantem a busca na lista D!")
        print('3.1 - Intersect(D, Q, %d, %d, %d, %d)' % (midD, maxD, midQ + 1, maxQ))
        Intersect(D, Q, midD, maxD, midQ + 1, maxQ, result)
        print("")
    else:
        print("Inverte a busca! Busca na lista Q!")
        print('3.2 - Intersect(Q, D, %d, %d, %d, %d)' % (midQ + 1, maxQ, midD, maxD))
        Intersect(Q, D, midQ + 1, maxQ, midD, maxD, result)
        print("")


    return result #Retorna o vetor interseccao


#Testes

#D = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 30, 40, 50, 60, 70, 80, 90, 100]
#Q = [2,10, 17, 30, 70, 90, 100, 101, 102,103,107,110,230,235,1000]

#D = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 30, 40, 50, 60, 70, 80, 90, 100]
#Q = [1,2,3,4,5,10]

#D = [2, 4, 6, 8, 10]
#Q = [1, 2, 3, 4]

#D = [0, 1, 2, 3, 4, 5]
#Q = [0, 3, 5, 6, 7, 8]

#D = [1, 2, 3, 4, 5]
#Q = [1, 4, 5]

#D = list(range(0,2000))
#Q = [0, 100, 101, 234, 2001]

D = list(range(0,1000000))
Q = list(range(10,1000,2))

result = []
print("\nIntersect(D, Q, 0, %d, 0, %d, result)" %(len(D)-1, len(Q)-1))
result_intersect = (Intersect(D, Q, 0, len(D)-1, 0, len(Q)-1, result))

print("")
print("Resultado da Interseccao: ")
if len(result_intersect) > 0:
    print(result_intersect)
else:
    print("Conjunto Vazio!!!")
