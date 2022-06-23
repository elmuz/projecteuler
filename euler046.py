import math

def isprime(n):
    if n > 1:
        for i in range(2, round(math.sqrt(n)) + 1):
            if n % i == 0 and i != n:
                return False
        return True
    else:
        return False


goldbach = True
n = 33 # save some iterations...
while goldbach == True:
    for i in range(3, round(math.sqrt(n)) + 1, 2):
        if n % i == 0 and i != n:
            foundCombination = False
            for j in range(2, n - 2 + 1):
                if isprime(j):
                    if math.sqrt((n - j) / 2) % 1 == 0:
                        foundCombination = True
                        break
            if not foundCombination:
                goldbach = False
            break
    n += 2
print(str(n - 2))
