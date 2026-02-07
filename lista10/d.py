#procura a maior sequência que alterna entre apenas dois valores diferentes na lista.
def conta(a, b, l):
    ultimo = -1
    qtd = 0

    for x in l:
        if x == a or x == b:
            if x != ultimo:
                qtd += 1
                ultimo = x

    return qtd


n = int(input())
l = []

for x in range(n):
    l.append(int(input()))

max = 1

for i in range(n):
    for j in range(i + 1, n):
        if l[i] != l[j]:
            qtd = conta(l[i], l[j], l)
            if qtd > max:
                max = qtd

print(max)
