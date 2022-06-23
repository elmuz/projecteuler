import math

def is_prime(n: int):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def find_combo_of_primes(n: int) -> int:
    lookup = {}
    def _find_combo(n: int, min_i) -> int:
        if n < min_i:
            return 0
        if n <= 1:
            return 0
        if n <= 3:
            return 1
        out = 0
        for i in range(min_i, n // 2 + 1):
            if not is_prime(i):
                continue
            if (n - i, i) in lookup:
                a = lookup[(n - i, i)]
            else:
                a =  _find_combo(n - i, i)
                lookup[(n - i, i)] = a
            out += a
        return out + int(is_prime(n))

    return _find_combo(n, 1) - int(is_prime(n))


n_combo = 0
i = 0
while n_combo < 5000:
    i += 1
    n_combo = find_combo_of_primes(i)
print(i)