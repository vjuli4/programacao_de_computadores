def ocorrencias(lista, x):
    if len(lista)==1:
        return 0
    if x == lista[0]:
        return 1 + ocorrencias(lista[1:], x )
    else:
        return ocorrencias(lista[1:], x )

lista = list(map(int, input().split()))
x = int(input())
l=ocorrencias(lista,x)
print(l)