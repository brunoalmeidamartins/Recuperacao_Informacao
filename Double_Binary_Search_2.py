import time
'''
Verifica se um conjunto possui mais elementos que o outro subset(D) > subset(Q)
'''
def comparaConjuntos(D,Q,inicioD, fimD, inicioQ, fimQ):
    result = True
    vet_aux1 = []
    vet_aux2 = []
    for i in range(inicioD, fimD):
        vet_aux1.append(D[i])
    for i in range(inicioQ, fimQ):
        vet_aux1.append(Q[i])
    if len(vet_aux1) > len(vet_aux2):
        result = True
    else:
        result = False
    return result

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
    return [minD-1, -1] #Retorna a posicao mais alta depois do valor a ser encontrado \  ex: 5 entre 4 e 6; retorna a posicao do 6


'''
Funcao de Interseccao de duas listas ordenadas
'''
def Intersect(D, Q, minD, maxD, minQ, maxQ, result):
    if len(Q) == 0 or len(D) == 0: #Se alguma das listas for vazia, entao termina recursao e retorna o vetor vazio!!
        return []
    #Condicacao de parada da recursao
    if minD > maxD or minQ > maxQ:
        print("Para recursao")
        return
    midQ = round((minQ+maxQ) / 2) #Pega a posicao do elemento do meio
    midQval = Q[midQ] #Pega o valor do elemento do meio
    busca_binaria = BinSearch(midQval, D, minD, maxD) # Faz a busca binaria do elemento de Q no vetor D
    midD = busca_binaria[0] #Recebe a posicao do valor no Vetor D ou a proxima posicao se o elemento nao for encontrado


    '''
    Primeiro IF verifica se o subconjunto (D) > subconjunto (Q)
    Essa comparacacao eh feita pegando o maior elemento do subconjunto (D) e comparando com o maior elemento do subconjunto (Q)
    Caso nao seja, a logica da procura eh invertida
    '''
    print("")
    #print('1 - D[midD -1]:%d > Q[minQ]:%d ' % (D[midD - 1], Q[minQ]))
    #print('1 - D[midD -1]:%d > Q[minQ]:%d ' % (D[midD], Q[minQ]))
    #if D[midD - 1] > Q[midQ - 1]:
    #if D[midD-1] > Q[minQ]:
    #print("Resultado: ",comparaConjuntos(D,Q,minD, midD-1, minQ, midQ-1))
    #if D[midD-1] > Q[minQ]:
    #if comparaConjuntos(D,Q,minD, midD-1, minQ, midQ-1):
    if comparaConjuntos(D,Q,minD, midD, minQ, midQ):
        print('1.1 - D, Q, %d, %d, %d, %d' %( minD,midD - 1, minQ, midQ - 1))
        print(Intersect(D, Q, minD,midD - 1, minQ, midQ - 1, result))
        print("")
    else:
        print('1.2 - Q, D, %d, %d, %d, %d' % (minQ, midQ - 1, minD, midD - 1))
        print(Intersect(Q, D, minQ, midQ - 1, minD, midD - 1, result))
        print("")

    '''
    Segundo IF verifica se o valor encontrado no vetor D eh o mesmo de do vetor Q
    Se sim, entao adiciona o valor a resposta, pois corresponde a uma interseccao 
    '''
    print("")
    #print('2 - D[midD]:%d == midQval:%d ' % (D[midD], midQval))
    if D[midD] == midQval:
        print("2.1 - Adicionando o resultado no vetor")
        result.append(midQval)
        midD = midD - 1
        print("")

    '''
    Terceiro IF verifica se o subconjunto (D) > subconjunto (Q)
    Essa comparacacao eh feita pegando o maior elemento do subconjunto (D) e comparando com o menor elemento do subconjunto (Q)
    Caso nao seja, a logica da procura eh invertida
    '''
    print("")
    #print('3 - D[maxD]:%d > Q[midQ]:%d ' % (D[maxD], Q[midQ]))
    #print(comparaConjuntos(D, Q, midD+1,maxD,midQ+1,maxQ))
    #if D[maxD] > Q[midQ]:
    #if comparaConjuntos(D, Q, midD+1,maxD,midQ+1,maxQ):
    if comparaConjuntos(D, Q, midD,maxD,midQ,maxQ):
    #if D[maxD] > Q[maxQ]:
        print('3.1 - D, Q, %d, %d, %d, %d' % (midD, maxD, midQ + 1, maxQ))
        print(Intersect(D, Q, midD, maxD, midQ + 1, maxQ, result))
        print("")
    else:
        print('3.2 - Q, D, %d, %d, %d, %d' % (midQ + 1, maxQ, midD, maxD))
        print(Intersect(Q, D, midQ + 1, maxQ, midD, maxD, result))
        print("")


    return result #Retorna o vetor interseccao


#Testes

'''
#vetor = list(range(0,10))
vetor = [10, 11, 12, 13, 14, 15, 17, 18, 19]
print(vetor)
chave = 16
posicao = BinSearch(chave, vetor, 0, len(vetor) - 1)

print(posicao)
#if posicao[1] >=0:
#    print("O elemento foi encontrado. Indice: ", posicao[1])
#else:
#    print("Elemento nao encontrado: ", posicao[0]) #Maior elemento depois da busca
'''


D = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 30, 40, 50, 60, 70, 80, 90, 100]
#Q = [0, 1, 2, 3, 4, 5, 17, 30, 70, 90, 100]
Q = [20, 60, 101]
#Q = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 30, 40, 50, 60, 70, 80, 90, 100]
#D = [2, 4, 6, 8, 10]
#Q = [1, 2, 3, 4]
#D = [0, 1, 2, 3, 4, 5]
#Q = [0, 3, 5, 6, 7, 8]
#D = [0, 1, 2, 3]
#Q = [3]
result = []
result_intersect = (Intersect(D, Q, 0, len(D)-1, 0, len(Q)-1, result))

print("")
print("Resultado da Interseccao: ")
if len(result_intersect) > 0:
    print(result_intersect)
else:
    print("Conjunto Vazio!!!")
