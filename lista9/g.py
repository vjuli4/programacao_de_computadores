l = []
while True:
    s = input()

    if s == "*":
        break
    l.append(s)
    
for s in l:
    ref = s[0]

    if 'a' <= ref <= 'z':
        ref = chr(ord(ref) - 32)

    v = True

    for i in range(1, len(s)):
        if s[i-1] == ' ':
            c = s[i]

            if 'a' <= c <= 'z':
                c = chr(ord(c) - 32)

            if c != ref:
                v = False
                break

    if v:
        print("Y")
    else:
        print("N")
