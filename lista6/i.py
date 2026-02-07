def lista_troca_menor_primeiro(lista):
    indice = lista.index(min(lista))
    if min(lista)==lista[0]:
        return 0
    else: 
#pegar o indice que o min estava e atribuir o valor o antigo 1º num da lista
        lista[0], lista[indice] = lista[indice], lista[0]
        return 1


lista = list(map(int,input().split()))
r = lista_troca_menor_primeiro(lista)
print (lista)
print(r)


