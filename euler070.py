import itertools
import math
from typing import Dict, List, Set


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def phi(n: int, primes: List[int], divisors: Dict[int, Set[int]]) -> int:
    if n < 2:
        return 0

    # Find divisors for a number `n`.
    # E.g. 5: {5}, 6: {2, 3}, 8: {2}, ....

    divisor_set = set()
    if len(primes) == 0:
        primes.append(2)
        divisors[2] = {2}
        return 1
    p_idx = 0
    p = primes[p_idx]
    m = n
    found_divisors = False
    while m != 1:
        while m % p == 0:
            m = m // p
            divisor_set.add(p)
            if m in divisors:
                divisor_set = divisor_set.union(divisors[m])
                found_divisors = True
                m = 1
                break
        if found_divisors:
            break
        if p_idx < len(primes) - 1:
            p_idx += 1
            p = primes[p_idx]
            if p > math.isqrt(m):
                primes.append(m)
                divisor_set.add(m)
                m = 1
        else:
            primes.append(m)
            divisor_set.add(m)
            m = 1
    divisors[n] = divisor_set

    # Find all coprimes for a given number `n`.
    # The idea is to count all the permutations of its divisors.
    # It is important to count numbers which share divisors exactly once.
    not_coprimes = 0
    for factors in itertools.product([0, 1], repeat=len(divisor_set)):
        divisor = 1
        num_factors = 0
        for idx, factor in enumerate(factors):
            if factor == 1:
                num_factors += 1
                divisor *= list(divisor_set)[idx]
        if divisor == 1:
            continue
        if num_factors % 2 == 1:
            not_coprimes += (n // divisor - 1)
        else:
            not_coprimes -= (n // divisor - 1)
    return n - 1 - not_coprimes


def is_permutation(n: int, m: int) -> bool:
    if sorted(str(n)) == sorted(str(m)):
        return True
    else:
        return False


if __name__ == '__main__':

    best_n = 1
    phi_of_best = 1
    best_ratio = float("Inf")
    limit = int(1e7)

    primes = []
    divisors = {}

    for n in range(2, limit + 1):
        phi_n = phi(n, primes, divisors)
        if n / phi_n < best_ratio and is_permutation(n, phi_n):
            best_n = n
            phi_of_best = phi_n
            best_ratio = n / phi_n


    print(f"Best `n` is {best_n}, with {phi_of_best} coprimes and a ratio of {best_ratio}")
