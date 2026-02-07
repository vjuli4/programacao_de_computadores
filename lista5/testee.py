a, b, c, d = map(int, input().split())

if a%2==0 and a<=b and a<=c and a<=d:
    print(a)

elif b%2==0 and b<=a and b<=c and b<=d:
    print(b)

elif c%2==0 and c<=a and c<=b and c<=d:
    print(c)

elif d%2==0 and d<=a and d<=b and d<=c:
    print(d)

else:
    print("0")