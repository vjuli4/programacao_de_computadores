def dia_da_semana (h,d):
    ii= 0
    ld = ["Domingo", "Segunda-feira", "Terca-feira", 
          "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"]
    if h == ld[0]:
        ii= 0

    elif h == ld[1]:
        ii= 1

    elif h == ld[2]:
        ii= 2

    elif h == ld[3]:
        ii= 3

    elif h == ld[4]:
        ii= 4

    elif h == ld[5]:
        ii= 5

    elif h == ld[6]:
        ii= 6

    c = (ii + d)%7
    return ld[c]

h = input()
d = int(input())
f = dia_da_semana(h,d)
print(f)