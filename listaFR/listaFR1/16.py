def junta(l1, l2):
    if len(l1)==0:
        return l2
    if len(l2)==0:
        return l1
    if l1[0] < l2[0]:
        return [l1[0]] + junta(l1[1:], l2)
    else:
        return [l2[0]] + junta(l1, l2[1:])



l1 = [1, 3, 11, 13]
l2 = [2, 4, 10, 12]
l=junta(l1, l2)
print(l)