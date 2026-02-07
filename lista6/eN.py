def dia_da_semana (h,d):
    ld = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"]
    indice_inicial = ld.index(h) # Pega o índice do dia inicial
    indice_final = (indice_inicial + d) % 7 # Calcula o índice final (usando módulo para reiniciar a semana)

    return ld[indice_final]  # Retorna o dia correspondente
    
h = input()
d = int(input())
c = dia_da_semana(h,d)
print(c)