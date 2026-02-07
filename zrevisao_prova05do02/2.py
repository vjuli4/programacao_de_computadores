def intercessao_i(l1,l2):
    s = 0
    for i in range(len(l1)):
        if i%2 ==0:
            if l[i] in l2:
                s += l[i]
    return s

l = list(map(int,input().split()))
ll = list(map(int,input().split()))
print(intercessao_i(l,ll))