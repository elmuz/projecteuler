"""
N/D < 3/7, D <= 1e6, ? biggest(N)
"""
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


l = float("Inf")
best_n = 1
best_d = 1
j = 3 / 7
for d in range(10, 1000000 + 1):
    n = d * 3 // 7
    if not are_coprime(n, d):
        continue
    f = n / d
    if abs(f - j)  < l:
        l = 3 / 7 - n / d
        best_n = n
        best_d = d
print(f"{best_n}/{best_d}, delta: {l}")


