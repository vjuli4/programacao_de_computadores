def conta_freq(lista, n):
    c = 0
    for i in range(len(lista)):
        if n == lista[i] and lista[i]%2==1:
            c +=1
    return c

n = int(input())
l = list(map(int,input().split()))
print(conta_freq(l, n))