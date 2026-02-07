def conta_algarismos(n):
    if n < 10:
        return 1
    else:
        return 1+conta_algarismos((n//10))
    

n = int(input())
a = conta_algarismos(n)
print(a)