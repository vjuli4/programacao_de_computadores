#a)desenhar árvore de chamada f (1,8)

#b)
def f(x,y):
    if (x>=y):
        return (x+y)/2
    else:
        return f(f(x+2,y-1),f(x+1,y-2))
    
x = int(input())
y = int(input())
c = f(x,y)
print(c)

#c)média aritimética