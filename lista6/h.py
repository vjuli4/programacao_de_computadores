def media_lista (lista):
    return sum(lista)//len(lista)

l = list(map(int, input().split()))
print(l)
media = media_lista(l)
print(media)
