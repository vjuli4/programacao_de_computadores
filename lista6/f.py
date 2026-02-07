def media_ponderada(v1,p1,v2,p2):
    mp = (v1*p1 + v2*p2) / (p1+p2)
    return mp

mp = media_ponderada(10,2,20,3)
print("{:.6f}".format(mp))