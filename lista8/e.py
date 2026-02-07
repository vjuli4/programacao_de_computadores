n = int(input())
ll = []
for i in range (1, n+1):
    c = 0
    l = float(input())

    while l>1.0:
        l = l/2
        c+=1
    ll.append(c)

for i in range (0, n):
    print(ll[i], "dias")



