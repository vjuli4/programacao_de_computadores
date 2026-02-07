def primo_rec(n, d):
    if d == 1:
        return True
    if n % d == 0:
        return False
    return primo_rec(n, d-1)

def primo(n):
    return primo_rec(n, n-1)

def primos(lista):
    if len(lista)==1:
        if primo(lista[0]):
            return lista
        else:
            return []
    if len(lista)>1:
        l = primos(lista[:-1])
        if primo(lista[-1]):
            l.append(lista[-1])
            return l
        else:
            return l
        
lista = list(map(int, input().split()))
l=primos(lista)
print(l)