from operator import mul

# 49/98 = 4/8
# If you don't include trivial examples only crossed reductions are allowed

N = []
D = []

for denominator in range(11,100): # only 2-digits fraction with ratio < 1
    d1 = int(str(denominator)[0])
    d2 = int(str(denominator)[1])

    if d1 > d2 and d2 != 0: # otherwise will produce a ratio > 1
    
        # Possible reduction n1 == d2
        for numerator in range(d2 * 10 + 1, d2 * 20):
            n1 = int(str(numerator)[0])
            n2 = int(str(numerator)[1])

            f0 = numerator / denominator
            if n2 / d1 == f0:
                N.append(numerator)
                D.append(denominator)
                print(str(numerator) + '/' + str(denominator) + ' = ' + str(n2) + '/' + str(d1))
    
        # Possible reduction n2 == d1
        for numerator in range(10 + d1,100,10):
            n1 = int(str(numerator)[0])
            n2 = int(str(numerator)[1])

            f0 = numerator / denominator
            if n1 / d2 == f0:
                N.append(numerator)
                D.append(denominator)
                print(str(numerator) + '/' + str(denominator) + ' = ' + str(n1) + '/' + str(d2))

