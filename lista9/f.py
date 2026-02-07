def reduz(s):
    while len(s) > 1:
        soma = 0
        for ch in s:
            soma += int(ch)
        s = str(soma)
    return int(s)

l = []

while True:
    n, m = input().split()
    if n == "0" and m == "0":
        break
    l.append((n, m))
    
for n, m in l:
    dn = reduz(n)
    dm = reduz(m)

    if dn > dm:
        print(1)
    elif dm > dn:
        print(2)
    else:
        print(0)
   