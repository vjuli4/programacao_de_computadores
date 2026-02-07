hinicial = input()
hfinal = input ()
duracao = int(hfinal) - int(hinicial)
h = int(duracao // 60)
m = duracao%60
print(f"{h:d}:{m:02d}")