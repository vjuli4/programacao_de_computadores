#se a diferença entre todos os pares consecutivos formam a sequencia dos números entre 1 e n - 1

#fazer uma lista com a diferença e vê se ela satisfaz isso: entre 1 e n - 1
while True:
    try:
        l = list(map(int,input().split()))
        n = l[0]
        l = l[1:]
        sequencia = list(range(1,n))
        diferencas = []

        for i in range(1, n):
            x = abs(l[i-1] - l [i]) 
            diferencas.append(x) 

        if sorted(diferencas) == sequencia:
            print("Alegre")
        else:
            print("Nao alegre")

    except EOFError:
        break