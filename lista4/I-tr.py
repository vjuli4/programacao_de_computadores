a, b, c = map(int, input().split())
h = c
if (a>h) :
    h = a
if (b>h) :
    h = b

if (a + b > c and a + c > b and b + c > a) :
    if (h**2 < a**2 + b**2 and h**2 < a**2 + c**2 and h**2 < b**2 + c**2) :
        print("a")
    elif (h**2 == a**2 + b**2 or h**2 == a**2 + c**2 or h**2 == b**2 + c**2) :
        print("r")
    else:
        print("o")
else:
    print("n")
