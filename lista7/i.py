n = int(input())
g = 0

for i in range(1, n+1):
    v = int(input())
    if v != 1:
        g+=1
    
print(g)