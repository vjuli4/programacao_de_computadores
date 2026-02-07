codigo, quantidade = map(int, input().split())
if (codigo == 1):
        total = quantidade * 4.00
        print ("Total: R$ %.2f" % total)
elif (codigo == 2):
        total = quantidade * 4.50
        print ("Total: R$ %.2f" % total)
elif (codigo == 3):
        total = quantidade*5.00
        print ("Total: R$ %.2f" % total)
elif (codigo == 4):       
        total = quantidade * 2.00
        print ("Total: R$ %.2f" % total)
elif (codigo == 5):
        total = quantidade * 1.50
        print ("Total: R$ %.2f" % total)