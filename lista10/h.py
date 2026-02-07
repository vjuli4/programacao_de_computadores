a, b = map(int, input().split())
sa = list(map(int, input().split()))
sb = list(map(int, input().split()))
if len(sa) != a:
    sa = list(map(int, input().split()))
if len(sb) != b:
    sb = list(map(int, input().split()))

#se sb é uma sub sequencia de sa
#apenas se for do maior p menor e todos os n estiverem presentes

#l = []
#for i in range(len(sb)):
#   if sb[i] in sa:
#        l.append(sb[i])
#        if sorted(sb) == l:
#            print("S")
#    else:
#        print("N")

l = []
pos = 0  # posição atual na lista sa

for x in sb:
    # procurar x em sa a partir da posição pos
    for i in range(pos, len(sa)):
        if sa[i] == x:
            l.append(x)
            pos = i + 1  
            break
    else:
        print("N")
        break
else:
    print("S")


