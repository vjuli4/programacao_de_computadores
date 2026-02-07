c = 0
n, p = map(int, input().split()) #n de competidores e n minimo de pontos
for i in range(1, n+1):
    x , y = map(int, input().split())
    if (x+y) >= p:
        c+=1

print(c)

