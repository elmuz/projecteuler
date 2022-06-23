# Prendi le permutazioni di 9 cifre
# Gli unici prodotti validi sono quelli
# di 4 cifre tra fattori di 2-3 o 1-4.

# Per ogni permutazione tenta i due split
# possibili per le cifre e controlla il
# prodotto. In caso affermativo salvalo.

import itertools

counter = 0

perms = itertools.permutations(str(123456789))

prods = []

for i in [''.join(x) for x in perms]:
    prod = int(i[5:])
    f1 =  int(i[0])
    f2 =  int(i[1:5])
    if f1 * f2 == prod:
        if prod not in prods:
            print(str(f1) + ' * ' + str(f2) + ' = ' + str(prod))
            counter += prod
            prods.append(prod)
    f1 = int(i[0:2])
    f2 = int(i[2:5])
    if f1 * f2 == prod:
        if prod not in prods:
            counter += prod
            prods.append(prod)
            print(str(f1) + ' * ' + str(f2) + ' = ' + str(prod))
prods.sort()
#print(prods)
print(counter)

