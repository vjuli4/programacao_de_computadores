#6. (20 pontos) Escreva uma função recursiva chamada eh_ordenada(lista). A
#função deve retornar True se a lista estiver ordenada em ordem crescente (ou seja,
#cada elemento é maior ou igual ao anterior) e False caso contrário.

#ERRADA! RECURSIVAAAA!!!!!!!!!

def eh_ordenada(lista):
    o = False
    c = 0
    for i in range(1, len(lista)):
        if lista[i] >= list[i-1]:
            c+=1
        if c == len(lista):
            o = True
    return o