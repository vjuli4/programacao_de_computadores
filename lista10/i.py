n = int(input())
seq = list(map(int, input().split()))

if n <= 2:
    print(1)
else:
    pas = [0] * n
    pas[0] = 1
    pas[1] = 1

    for i in range(2, n):
        if seq[i] - seq[i-1] == seq[i-1] - seq[i-2]:
            pas[i] = pas[i-1]
        else:
            pas[i] = pas[i-2] + 1

    print(pas[n-1])
