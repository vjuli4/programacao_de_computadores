#Escreva um programa, em Python, que leia 2 números inteiros e mostre o
#maior, o menor e a diferença entre eles (necessariamente nessa ordem).
a = int(input())
b = int(input())
c=a

if a>b:
    c=a
    print("maior:",c)
    print("menor:",b)
    diferenca = c-b
    print("diferença:",diferenca)
elif b>a:
    c=b
    print("maior:",c)
    print("menor:",a)
    diferenca = c-a
    print("diferença:",diferenca)


