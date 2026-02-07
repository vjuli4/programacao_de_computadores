def maior5 (a,b,c, d, e):
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    if d > maior:
        maior = d
    if e > maior:
        maior = e
    return maior

m = maior5(1,6,9,7,3)
print(m)