#lista com divisores de n
def divisores_rec(n, k):
    if k == 1:
        return [1]
    lista = divisores_rec(n, k-1)
    if n % k == 0:
        lista.append(k)
    return lista

def divisores(n):
    return divisores_rec(n, n)

n = int(input())
d = divisores(n)
print(d)