tabuleiro = []
for i in range(10):
    tabuleiro.append([0] * 10)

qnt = int(input())
v = True

for _ in range(qnt):
    dir, tam, lin, col = map(int, input().split())

    lin -= 1
    col -= 1

    if dir == 0:
        for c in range(col, col + tam):
            if c >= 10 or tabuleiro[lin][c] == 1:
                v = False
                break
            tabuleiro[lin][c] = 1
    else:
        for l in range(lin, lin + tam):
            if l >= 10 or tabuleiro[l][col] == 1:
                v = False
                break
            tabuleiro[l][col] = 1

    if not v:
        break

if v:
    print("Y")
else:
    print("N")
