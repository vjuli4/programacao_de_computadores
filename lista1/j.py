n = int(input())

qn_100 = n // 100
resto_100 = n%100

qn_50 = resto_100 // 50
resto_50 = resto_100 %50

qn_20 = resto_50 // 20
resto_20 = resto_50 %20

qn_10 = resto_20 // 10
resto_10 = resto_20 %10

qn_5 = resto_10 // 5
resto_5 = resto_10 %5

qn_2 = resto_5 // 2
resto_2 = resto_5 %2

qn_1 = resto_2 // 1
resto_1 = resto_2 %1


print(n) 
print(qn_100, "nota(s) de R$ 100,00")
print(qn_50, "nota(s) de R$ 50,00")
print(qn_20, "nota(s) de R$ 20,00")
print(qn_10, "nota(s) de R$ 10,00")
print(qn_5, "nota(s) de R$ 5,00")
print(qn_2, "nota(s) de R$ 2,00")
print(qn_1, "nota(s) de R$ 1,00")
 