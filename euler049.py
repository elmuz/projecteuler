import math
import itertools

def isprime(n):
    if n > 1:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0 and i != n:
                return False
        return True
    else:
        return False

sequences = 0

for c in itertools.combinations_with_replacement('0123456789', 4):
    
    # Check if all digits are even.
    # In that case primes are possible
    even = True
    for d in range(len(c)):
        if int(list(c)[d]) % 2 == 1:
            even = False
            break
    if even:
        continue

    primes = set()

    for p in itertools.permutations(c):
        if len(str(int(''.join(list(p))))) == 4 and isprime(int(''.join(list(p)))):
            primes.add(int(''.join(list(p))))

    primes = list(primes)
    primes.sort()

    if len(primes) > 2:
        for i in range(len(primes)):
            for j in range(i + 1, len(primes)):
                d1 = primes[j] - primes[i]
                for k in range(j + 1, len(primes)):
                    d2 = primes[k] - primes[j]
                    if d1 == d2:
                        print(primes[i], primes[j], primes[k], str(primes[i]) + str(primes[j]) + str(primes[k]))


