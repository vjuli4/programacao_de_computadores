a, b = map(int, input().split())
m = 0
for i in range (1, b+1) :
    m = a*i
    l = []
    if m<=b:
        l.append(m)
        print(*l, end=" ")

        
