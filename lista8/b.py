s, m = map(int,input().split())
c = 0

while m >= 0.5:
    m = m/2
    c+=1

#segundos totais
seg = s*c
#dias (total/dia*hora*min)
d = seg//(24*60*60)
r = seg%(24*60*60) #resto

#horas (resto de dias/hora*min)
h= r//(60*60)
r = r%(60*60) #resto

#minutos (resto de horas/min)
m = r//60
r = r%60 #resto (SEGUNDOS)

print(f"{d} dias {h:02}:{m:02}:{r:02.0f}")