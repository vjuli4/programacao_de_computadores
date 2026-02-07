#EXERCÍCIO 2
v_a = float (input("Digite seu salário atual: "))
p_r = float (input("Digite o percentual de ajuste: "))
reajuste = (p_r/100*v_a)+v_a
print ("Atual: {:.2f}".format(v_a))
print ("Reajustado: {:.2f}".format(reajuste))