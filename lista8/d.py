#menor numero primo maior que n
n = int(input())
x = n+1
while True: 
    qtd = 0
    for i in range(1, x+1):
        if x % i == 0:
            qtd+=1
    if qtd == 2:
        print(x)
        break
    
    x+=1