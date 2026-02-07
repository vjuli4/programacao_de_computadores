def diaa(dia,mes,ano):
    dias=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    meses = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    if not (1 <= mes <= 12 and ano <= 10000 and 1<=dia<=dias[mes-1]):
        return "Data Invalida"
    else:
        return f"{dia:02d} de {meses [mes - 1]} de {ano}"
        

data = input().strip()
dia, mes, ano = map(int,data.split("/"))
c = diaa (dia,mes,ano)
print(c)
