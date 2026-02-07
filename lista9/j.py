n = int(input())
k = int(input())

p = []
for _ in range(n):
    p.append(int(input()))

p.sort()

nota_corte = p[n - k]

c = 0
for x in p:
    if x >= nota_corte:
        c += 1

print(c)
