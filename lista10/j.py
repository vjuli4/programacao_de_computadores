n = int(input())
pilhas = list(map(int, input().split()))

p = sum(pilhas)
r = -1

for i in range(min(pilhas) + 1):
    escada = []
    for j in range(n):
        escada.append(i + j)

    if sum(escada) != p:
        continue

    m = 0
    for j in range(n):
        if pilhas[j] > escada[j]:
            m += pilhas[j] - escada[j]

    if r == -1 or m < r:
        r = m

print(r)
