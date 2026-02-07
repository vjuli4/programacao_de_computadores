def maior_salto(lista):
    l = []
    d = 0
    for i in range(1, len(lista)):
        d = abs(lista[i] - lista[i-1])
        l.append(d)
    ordenada = sorted(l)
    return ordenada[-1]

ll= list(map(int,input().split()))
print(maior_salto(ll))