#I1 = a / I2 = a e b

n = int(input())
l = list(map(int, input().split()))

a = 0
b = 0
for i in range(n):
    if l[i] == 1:
        a ^= 1
    elif l[i] == 2:
        a ^= 1
        b ^= 1

print(a)
print(b)