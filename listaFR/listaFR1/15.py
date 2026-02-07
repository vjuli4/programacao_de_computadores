def polinomio(coeficientes, x):
    if len(coeficientes)==1:
        return coeficientes[0]
    else: 
        return x * polinomio(coeficientes[:-1],x) + coeficientes[-1]
    
coeficientes = [2, 6, 3, 4, 5]
x = 10
r = polinomio(coeficientes, x)
print(r)