a = int (input())
b = int (input())
c = int (input())

#acelerado
if (b-a) < (c-b):
    print("1")

#desacelerado
elif (b-a) > (c-b):
    print("-1")

#manter a velocidade
elif (b-a) == (c-b):
    print("0")
