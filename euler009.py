import math

for a in range(1,1000):
    for b in range(a, 1000):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print('a: ' + str(a) + ', b: ' + str(b) + ', c: ' + str(c) + ', abc: '+ str(a*b*c))
            exit(0)
