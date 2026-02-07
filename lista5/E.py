n = int(input())

total=0
if (n<=10):
    total = 7
if (11<=n<=30):
    intervalo = n-10
    preco = 1
    total = 7 + (intervalo*preco)
if (31<=n<=100):
    intervalo = n-30
    preco = 2
    total = 7 + 20 + (intervalo*preco)
if (n>100):
    intervalo = n-100
    preco = 5
    total = 7 + 20 + 140 + (intervalo*preco)

print(total)