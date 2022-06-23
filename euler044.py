hop = 1
P = [0, 1]

def pentagons_lovers():
    n = 2
    while True:
        Pn = int(n * (3 * n - 1) / 2)
        P.append(Pn)
        hop = P[-1] - P[-2]
    
        # Search candidates for P(i) - P(j)
        # Check only numbers greater than last hop
        lowers = [i for i in P[:-1] if i >= hop]
        for Pj in lowers:
            if Pn - Pj in P:
                print('P(' + str(n) + ') = ' + str(Pn) + ', hop = ' + str(hop))     
                # Check P(i) + P(j) knowing that 'hop' gets higher of 3 at any step
                hop_test = hop + 3
                while hop_test <= Pj:
                    if hop_test == Pj:
                        # Both sum and difference are pentagonal
                        #if D > Pn - Pj:
                        #    D = Pn - Pj
                        print('n = ' + str(n) + ', P(n) = ' + str(Pn) + ', P(j) = ' + str(Pj))
                        return Pn - Pj
                    else:
                        hop_test += hop_test + 3
        n += 1
"""
def pentagons_lovers():
    P[1]
    hop = 1
    n = 2
    while True:
        P.append(int(n * (3 * n - 1) / 2))
        hop += 3
"""
pentagons_lovers()
