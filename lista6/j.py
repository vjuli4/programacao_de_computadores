def sublista_sem_menor(lista):
    l=lista.copy()
    l.remove(min(lista))
    return l

#criar nova lista(mesma ordem) - min(lista)

lista = list(map(int,input().split()))
r = sublista_sem_menor(lista)
print(r)