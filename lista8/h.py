n = int(input())
l = []

while n != 0:
    h = list(map(int, input().split()))
    p = 0

    for i in range(0, n):
        e = h[i - 1]
        d = h[(i + 1) % n]

        if h[i] > e and h[i] > d:
            p = p + 1 
        elif h[i] < e and h[i] < d:
            p = p + 1
    l.append(p)
    n = int(input())
for i in range(0, len(l)):
    print(l[i])