import math

def isprime(n):
    if n > 1:
        for i in range(2, round(math.sqrt(n)) + 1):
            if n % i == 0 and i != n:
                return False
        return True
    elif n == 1:
        return True
    else:
        return False

def shift(n):
    return int(str(n)[1:] + str(n)[0])

counter = 0

for i in range(2,1000000):
    if '0' in str(i):
        continue
    if isprime(i):
        circular = True
        n = i
        for j in range(len(str(i)) - 1):
            n = shift(n)
            if not isprime(n):
                circular = False
                break
        if circular:
            print(i)
            counter += 1

print('Total ' + str(counter))
