def conta_bits(n):
#2**0=1, 2**1=2
    if n < 2:
        return 1
    else:
        return 1+conta_bits((n//2))
    

n = int(input())
a = conta_bits(n)
print(a)