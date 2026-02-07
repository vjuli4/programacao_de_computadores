#se ele for divisivel apenas por 1 e ele mesmo
n = int(input())
qtd = 0
for i in range(1, n+1):
    if n % i == 0:
        qtd = qtd + 1
if qtd == 2:
        print("Sim")
else:
        print("Nao")