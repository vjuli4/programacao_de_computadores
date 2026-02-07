l = []
c = 0

n = int(input()) #tamanhos totais
for tamanhos in range (1, n+1):
    nn = int(input()) #qtd tamanhos
    l.append(nn)


p = int(input()) #pedidos totais
for pedidos in range (1, p+1):
    i = int(input()) #tamanho pedido pelo cliente
        #l = 4 0 2 3 2
        #l = 1 3 2 5
        #so vai vender quando l[pedidos] for maior que i
    if l[i-1] > 0:
        c+=1
        l[i-1]-=1
        #atualiza l
print(c)

            
