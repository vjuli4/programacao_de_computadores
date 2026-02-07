c_estrada, dist = map(int, input().split())
cust_km, valor_ped = map(int, input().split())
custo_km = c_estrada * cust_km
qnt_ped = c_estrada//dist 
custo_ped = qnt_ped * valor_ped
custototal = custo_km  + custo_ped
print(custototal)