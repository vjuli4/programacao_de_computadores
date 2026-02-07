n = int(input())
v = []
qm = 1
for _ in range(n):
    v.append(int(input()))

for i in range(len(v)-1):
    if v[i] != v[i+1]:
        qm+=1
print(qm)

