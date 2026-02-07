def indice_do_maior(lista):
    if len(lista)==1:
        return 0
    i = indice_do_maior(lista[:-1])
    if lista[-1] > lista[i]:
        i = len(lista)-1
    return i




lista = list(map(int, input().split()))
l=indice_do_maior(lista)
print(l)