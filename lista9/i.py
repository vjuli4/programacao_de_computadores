e = []

while True:
    n = int(input())
    if n == 0:
        break

    r = []
    for _ in range(n):
        x, y, u, v = map(int, input().split())
        r.append((x, y, u, v))

    e.append(r)

t = 1
for r in e:
    X = -100000
    Y = 100000
    U = 100000
    V = -100000

    for x, y, u, v in r:
        if x > X:
            X = x
        if y < Y:
            Y = y
        if u < U:
            U = u
        if v > V:
            V = v

    print(f"Teste {t}")

    if X <= U and Y >= V:
        print(X, Y, U, V)
    else:
        print("nenhum")

    print()
    t += 1
