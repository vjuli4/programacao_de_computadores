t = int(input())
l = []

for i in range(1, t+1):
    d, n = map(int, input().split())
    p = list(map(float, input().split()))
    lt = []
    for ind in range(0, n):
        if p[ind] > d:
            tr = 0
        else:
            tr = d % p[ind]
        lt.append(tr)
    l.append(max(lt))
for t in range(0, len(l)):
    print(f"{l[t]:.02f}")