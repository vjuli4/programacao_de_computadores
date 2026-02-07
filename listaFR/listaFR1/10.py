def ordenada(lista):
    if len(lista)==1:
        return True
    if lista[0] < lista[1]:
        return ordenada(lista[1:])
    return False

lista = list(map(int, input().split()))
l=ordenada(lista)
print(l)