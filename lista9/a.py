j, r = map(int, input().split())
p = list(map(int, input().split()))

ptotais = [0]*j
i = 0
if len(p) == (j*r):
    for rodadas in range (r):
        for jogadores in range (j):
            ptotais[jogadores] += p[i]
            i+=1

    v = 0
    for vencedor in range(j):
        if ptotais[vencedor] >= ptotais[v]:
            v = vencedor
    print(v+1)
