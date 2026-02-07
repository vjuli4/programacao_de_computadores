n1 = int(input())
n2 = list(map(int,input().split()))
z = 0
y = 0
m = sum(n2)/n1
for i in range(n1): #percorre os índices de 0 até n1-1
    if n2[i]<m:
        z+=1
    else:
        y+=1
print("{:.1f}".format(m))
print(z)
print(y)