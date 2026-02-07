n = int(input())
s = str(input())

t = 0
c = 1

for i in range(1, n):
    if s[i] == s[i-1]:
        c += 1
    else:
        if s[i-1] == 'a' and c >= 2:
            t += c
        c = 1

# último bloco
if s[n-1] == 'a' and c >= 2:
    t += c

print(t)
