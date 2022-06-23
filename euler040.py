counter = 0
n = 0
prod = 1
d100 = False
d1000 = False
d10000 = False
d100000 = False

while counter < 1000000:
    n += 1
    counter += len(str(n))

    if counter >= 100 and not d100:
        p = int(str(n)[len(str(n)) - 1 - (counter - 100)])
        d100 = True
        prod *= p
    elif counter >= 1000 and not d1000:
        p = int(str(n)[len(str(n)) - 1 - (counter - 1000)])
        d1000 = True
        prod *= p
    elif counter >= 10000 and not d10000:
        p = int(str(n)[len(str(n)) - 1 - (counter - 10000)])
        d10000 = True
        prod *= p
    elif counter >= 100000 and not d100000:
        p = int(str(n)[len(str(n)) - 1 - (counter - 100000)])
        d100000 = True
        prod *= p

p = int(str(n)[len(str(n)) - 1 - (counter - 1000000)])
prod *= p

print(prod)
        
