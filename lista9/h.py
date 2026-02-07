n = int(input())
v = list(map(int, input().split()))

# se tiver 1 ou 2 números, sempre existe só 1 escadinha
if n <= 2:
    print(1)
else:
    c = 1  # pelo menos uma escadinha existe
    dif = v[1] - v[0]

    for i in range(2, n):
        nova_dif = v[i] - v[i-1]

        if nova_dif != dif:
            c += 1
            dif = nova_dif

    print(c)
