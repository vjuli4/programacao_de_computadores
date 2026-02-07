m = int(input())
a = int(input())
b = int(input())

d = m - (a + b)

if a>b and a>d:
    print(a)
elif b>a and b>d:
    print(b)
elif d>a and d>b:
    print(d)