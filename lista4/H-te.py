c = int(input())
a = int(input())
z = a // (c-1)
if (a % (c-1) != 0):
    z = z + 1
print(z)
