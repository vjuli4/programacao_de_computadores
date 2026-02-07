def inverter_lista_rec(lista, inicio, fim):
    if inicio>=fim:
        return lista
    else:
        lista[inicio], lista[fim] = lista[fim],  lista[inicio]
        return inverter_lista_rec(lista, inicio+1, fim-1)
    
def inverter_lista(lista):
    inicio = 0
    fim = len(lista) - 1
    return inverter_lista_rec(lista, inicio, fim) 

lista = list(map(int, input().split()))
l=inverter_lista(lista)
print(l)   
#lista[1:]=lista[:1], lista[2:]=lista[:2]
#lista[3:]=lista[:3] 1 5 6