def BinSearch(midQval, D, minD, maxD): #Retorna posicao
    #Condicao de parada
    #q = 0
    if minD <= maxD:
        q = (minD + maxD) // 2
        if midQval > D[q]:
            return BinSearch(midQval, D, q+1, maxD)
        elif midQval < D[q]:
            return BinSearch(midQval, D, minD, q - 1)
        else:
            return [q, midQval] #Retorna a posicao e valor ## Achou o valor midQval
    return [minD, -1] #Nao encontrado # Retorna a posicao mais alta depois do valor a ser encontrado \  ex: 5 entre 4 e 6; retorna a posicao do 6



def Intersect(D, Q, minD, maxD, minQ, maxQ, result):
    if len(Q) == 0 or len(D) == 0:
        return
    if minD > maxD or minQ > maxQ:
        return
    midQ = round((minQ+maxQ) / 2)
    midQval = Q[midQ]
    busca_binaria = BinSearch(midQval, D, minD, maxD)
    midD = busca_binaria[0]
    ##if D[midD - 1] > Q[midQ - 1]:
    #if D[midD] > Q[midQ]:
    #verifica_subconjunto(D, Q, minD, minD - 1, minQ, minQ - 1)
    if D[midD] > Q[midQ - 1]:
        #result = result + Intersect(D, Q, minD - 1, minQ, midQ - 1)
        valor = Intersect(D, Q, minD,midD - 1, minQ, midQ - 1, result)
        if valor is not None:
            #result.append(valor)
            pass
    else:
        #result = result + Intersect(Q, D, minQ, midQ - 1, minD, midD - 1)
        valor = Intersect(Q, D, minQ, midQ - 1, minD, midD - 1, result)
        if valor is not None:
            #result.append(valor)
            pass
    if D[midD] == midQval:
        #result = result + midQval
        result.append(midQval)
        midD = midD - 1
        #midD = midD
    if D[maxD] > Q[midQ]:
    #if D[maxD] > Q[maxQ]:
    #if D[midD] > Q[midQ]:
    #if D[midD+1] > Q[maxQ]:
        #result = result + Intersect(D, Q, midD, maxD, midQ + 1, maxQ)
        valor = Intersect(D, Q, midD, maxD, midQ + 1, maxQ, result)
        if valor is not None:
            #result.append(valor)
            pass
    else:
        #result = result + Intersect(Q, D, midQ + 1, maxQ, midD, maxD)
        valor = Intersect(Q, D, midQ + 1, maxQ, midD, maxD, result)
        if valor is not None:
            #result.append(valor)
            pass
    return result


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
#Q = [1, 13,17]
Q = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 30, 40, 50, 60, 70, 80, 90, 100]
result = []
print(Intersect(D, Q, 0, len(D) - 1, 0, len(Q) - 1, result))