def compactar(lista):
    if len(lista) == 0:
        return []
    
    r = [lista[0]]
    for i in range(1, len(lista)):
        if lista[i] != lista[i-1]:
            r.append(lista[i])
    return r

l = list(map(int,input().split()))
print(compactar(l))
