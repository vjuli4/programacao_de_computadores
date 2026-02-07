#inverter valor compara se fica igual
#recursiva q entre a palavra e a invertida

# def palimdromo(s):
#     i = s[::-1]
#     if s == i:
#         return print(s, "é um palimdromo")
#     else:
#         return print("O contrario de"+s+"é"+i+". Não são iguais, logo não é um palimdromo")
def inverter(s):
    if len(s) <= 1:
        return s
    return s[-1] + inverter(s[:-1])

def palindromo(s):
    i = inverter(s)
    if s == i:
        return "É um palindromo"
    else:
        return "Não é um palindromo"
s = input()
p = palindromo(s)
print(p)