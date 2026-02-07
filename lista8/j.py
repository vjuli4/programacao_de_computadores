n, r = map(int,input().split()) 
rr = list(map(int,input().split())) 
v = []

if r == n:
    print("*")
else:
    for i in range(1, n + 1):
        if i not in rr:
            v.append(i)

    for item in v:
        print(item, end=" ")
    print()