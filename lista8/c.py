#sempre começa do cano mais a esquerda
#sobrevive apenas se canoA - canoP <= p
#se canoP > p ele cai
#se canoP for muito baixo não agenta a queda
#dadas as alturas dos canos e a altura do pulo do sapo, mostra se a fase do jogo pode ser vencida ou não.

p, nc = map(int, input().split())
n = list(map(int,input().split()))
i = 0
 
while i < nc-1 :
    d = abs(n[i] - n[i+1])
    if d > p:
        print("GAME OVER")
        break
    i+=1
 
else:
    print("YOU WIN")

