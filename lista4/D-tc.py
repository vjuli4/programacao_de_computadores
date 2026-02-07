
consumodcarro = int(input())
distanciaaero = int(input())
tlitrosantes = int(input())
t = distanciaaero / consumodcarro
qc = t - tlitrosantes
z = 0
if (t > tlitrosantes):
    print("{:.1f}".format(qc))
else:
    if (qc <= 0):
        print("{:.1f}".format(z))
