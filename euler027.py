import math
def isprime(n):
    if n < 1:
        return False
    if n != 1:
        for i in range(2, round(math.sqrt(n)) + 1):
            if n % i == 0 and i != n:
                return False
        return True
    else:
        return True

longest = 0
prod = 0
for a in range(-999,1000):
    for b in range(-1000,1001):
        counter = 0
        n = 0
        f = n**2 + a*n + b
        while isprime(f):
            counter += 1
            n += 1
            f = n**2 + a*n + b
        if counter > longest:
            longest = counter
            prod = a * b
print(prod)



