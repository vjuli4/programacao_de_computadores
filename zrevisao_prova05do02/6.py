#5. (20 pontos) Escreva uma função chamada conta_picos(lista) que receba uma lista de
#números inteiros. A função deve retornar a quantidade de elementos que são estritamente maiores
#que seus dois vizinhos imediatos (o anterior e o posterior).

def conta_picos(lista):
    picos = 0
    for i in range(1,len(lista)-1):
        if lista[i] > lista[i-1] and lista[i] > lista[i+1]:
            picos+=1
    return picos

l = list(map(int,input().split()))
print(conta_picos(l))