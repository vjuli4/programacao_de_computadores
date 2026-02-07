distancia = int(input())
velocidade = int(input())
tempo = distancia / velocidade
tempoh = distancia // velocidade
tempom = (tempo - tempoh) * 60
print("{:02d}:{:02d}".format(tempoh, int(tempom)))