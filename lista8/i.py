c = 0
senhas = []
while True:
    try:
        n = int(input())
        v = list(map(float, input().split()))
        c+=1

        senha = ""
        for i in range(0, n):
            im = v.index(max(v))
            senha += str(im)
            v[im] = -1
            
        senhas.append(f"Caso {c}: {senha}") 
    except EOFError:
        break

for senha in senhas:
    print(senha)