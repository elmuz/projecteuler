import math

def are_coprime(a, b):
    if a == 1:
        if b == 1:
            return False
        else:
            return True

    for i in range(2, math.isqrt(a) + 1):
        if a % i == 0:
            if b % i == 0:
                return False
            while a % i == 0:
                a //= i
        if a == 1:
            return True
    if b % a == 0:
        return False
    return True


lbnd = 1 / 3
ubnd = 1 / 2
counter = 0
for d in range(4, 12000 + 1):

    # Check lower bound
    m = int(math.ceil(d * lbnd))

    # Find upper bound
    n = int(math.floor(d * ubnd))

    for i in range(m, n + 1):
        if are_coprime(i, d):
            counter += 1

print(counter)


