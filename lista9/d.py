c = str(input())
crib = str(input())
i = 0

for cc in range ((len(c) - len(crib))+1):
    v = True
    for ccrib in range (len(crib)):
        if c[cc+ccrib] == crib[ccrib]:
            v = False
            break
    if v:
        i += 1
print(i)            