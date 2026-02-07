def analista_crescimento(lista):
    ll = []
    for i in range(1, len(lista)):
        if lista[i] > lista[i-1]:
            ll.append(i)
    return ll

l = list(map(int,input().split()))
print(analista_crescimento(l))
