h1, m1, h2, m2 = map(int,input().split())

#while not (h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0):
while (h1!=0 or m1!=0 or h2!=0 or m2!=0):
    
    i = h1*60 + m1
    f = h2*60 + m2

    if f < i:
        f+=1440

    s = f - i
    print(s)

    h1, m1, h2, m2 = map(int,input().split())
    
    