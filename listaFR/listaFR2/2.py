def ackermann_c(m, n):
    qtd = 1
    if m == 0:
        return qtd
    if n == 0:
        return qtd + ackermann_c(m - 1, 1)
    else:
        qtd_m_n1 = ackermann_c(m, n - 1)
        qtd_m1_x = ackermann_c(m - 1, )
        
    return qtd + qtd_m1_x + qtd_m_n1

m, n = map(int,input().split())
n_chamadas_rec = ackermann_c(m, n)
print(n_chamadas_rec)