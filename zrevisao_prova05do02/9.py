def repetidos(lista):
    maior_qtd = 1
    qtd_atual = 1
    numero_maior = lista[0]
    inicio_maior = 0
    inicio_atual = 0

    for i in range(1, len(lista)):
        if lista[i] == lista[i-1]:
            qtd_atual += 1
        else:
            if qtd_atual > maior_qtd:
                maior_qtd = qtd_atual
                numero_maior = lista[i-1]
                inicio_maior = inicio_atual
            qtd_atual = 1
            inicio_atual = i

    # verificação final
    if qtd_atual > maior_qtd:
        maior_qtd = qtd_atual
        numero_maior = lista[-1]
        inicio_maior = inicio_atual

    return maior_qtd, numero_maior, inicio_maior
