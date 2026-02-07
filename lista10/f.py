#Primeiro for: conta distância indo pra direita
#Segundo for: vê se pela direita é menor e corrige

n = int(input())
l = list(map(int, input().split()))
if len(l) != n:
    l = list(map(int, input().split()))


for i in range(1, n):
    if l[i] == -1 and l[i - 1] != -1:
        l[i] = l[i - 1] + 1

for i in range(n - 2, -1, -1):
    if l[i] == -1 or l[i] > l[i + 1] + 1:
        if l[i + 1] != -1:
            l[i] = l[i + 1] + 1

for i in range(n):
    if l[i] > 9:
        l[i] = 9

print(*l)
