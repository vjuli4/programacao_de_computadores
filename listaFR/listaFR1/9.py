def soma_pares(lista):
    if len(lista)==1:
        if lista[0]%2==0:
            return lista[0]
        else:
            return 0
    if len(lista)>1:
        if (lista[-1]%2)==0:
            return soma_pares(lista[:-1]) + lista[-1]
        else:
            return soma_pares(lista[:-1])

        
            
        

lista = list(map(int, input().split()))
l=soma_pares(lista)
print(l)
