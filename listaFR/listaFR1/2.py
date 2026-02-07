def primo_rec(n, d):
    if d == 1:
        return True
    if n % d == 0:
        return False
    return primo_rec(n, d-1)


def primo(n):
    return primo_rec(n, n-1)
    

n = int(input())
eprimo = primo(n)
print(eprimo)

