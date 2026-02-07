#a quantidade média de batimentos cardíacos no exame realizado (media)
#a quantidade de medições com batimentos acima ou abaixo da média obtida (acima ou abaxio da media)
#considerando uma diferença de 10% entre cada valor medido e a média.

n = int(input()) #qtd de medições
l  = []
c = 0

for entrada in range (n):
    b = int(input()) #medições
    l.append(b)

media = sum(l)//len(l)
limiteB = int(media - (media * 0.1))
limiteC = int(media + (media * 0.1))

for i in range(n):
    if l[i] <  limiteB or l[i] >  limiteC:
        c+=1

print (media)
print(c)

