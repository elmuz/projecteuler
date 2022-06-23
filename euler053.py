import math

def ncr(n, r):
    if r == 0: return 1
    numer = math.factorial(n)
    denom = math.factorial(r) * math.factorial(n - r)
    return numer // denom

count = 0
for n in range(23, 101):
    for r in range(1, n):
        if ncr(n, r) > 1000000:
            count += 1
print(count)
