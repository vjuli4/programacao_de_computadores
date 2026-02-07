#maior repetiçao de uma letra
n = str(input())
r = 1
maior_r = 0
for i in range(1, len(n)):
    if n[i-1] == n[i]:
        r += 1
    else:
        if r > maior_r:
            maior_r = r
        r = 1
if r > maior_r:
    maior_r = r
print(maior_r)