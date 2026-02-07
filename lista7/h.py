#quantidade
c = int(input())
saldo =  100
m_saldo = 100

for i in range(1, c+1):
    v = int(input())
    saldo+=v

    if saldo > m_saldo:
        m_saldo = saldo
    
print(m_saldo)

"""c = int(input())
saldo =  100
m_saldo = 100
v = []

for _ in range(c):
    v.append(int(input()))

for i in range(c):
    saldo += v[i]

    if saldo > m_saldo:
        m_saldo = saldo
    
print(m_saldo)"""