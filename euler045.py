def Tri(n):
    return int(n * (n + 1) / 2)

def Pen(n):
    return int(n * (3 * n - 1) / 2)

def Hex(n):
    return int(n * (2 * n -1))

combo = 0
t = 0
p = 0
h = 0
while combo < 3:
    h += 1
    Pt = Tri(t)
    Pp = Pen(p)
    Ph = Hex(h)
    while Ph >= Pp:
        if Ph == Pp:
            while Pp >= Pt:
                if Pp == Pt:
                    combo += 1
                    print('T(' + str(t) + ') = P(' + str(p) + ') = H(' + str(h) + ') = ' + str(Pt))
                    t += 1
                    Pt = Tri(t)
                else:
                    t += 1
                    Pt = Tri(t)
            p += 1
            Pp = Pen(p)
        else:
            p += 1
            Pp = Pen(p)


