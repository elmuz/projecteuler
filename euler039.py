import math

count = 1001*[0]
for a in range(5, 500): # ipotenusa < metà perimetro
    for b in range(1, a): # cateto < ipotenusa
        for c in range(1, min(1000 - a - b, b + 1)):
            if a**2 == b**2 + c**2:
                count[a + b + c] += 1
                print(str(a) + '^2 = ' + str(b) + '^2 + ' + str(c) + '^2. p = ' + str(a + b + c))  

print(str(count.index(max(count))) + ',' + str(max(count)))
    
