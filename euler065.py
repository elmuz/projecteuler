import math
from typing import List, Tuple


# Each fraction can be written as:
#     sqrt(A) + B
# D + -----------
#          C
def sub_fraction(a_0: int, b_0: int, c_0: int) -> Tuple[int, int, int]:
    # Reciprocal
    numerator = c_0
    radicand = a_0
    minus = b_0

    # Rational
    multiplier = numerator
    # radicand = radicand
    addendum = -minus
    denominator = radicand - minus ** 2

    # Simplify
    assert denominator % multiplier == 0
    denominator = denominator // multiplier

    # Simplify
    s = int(math.sqrt(radicand) + addendum)
    d_1 = s // denominator
    remainder = s % denominator
    b_1 = addendum + remainder - s
    c_1 = denominator

    return d_1, b_1, c_1


def first_divisor(n: int) -> int:
    if n < 2:
        return False
    for i in range(2, int(math.floor(math.sqrt(n))) + 1):
        if n % i == 0:
            return i
    return n


def find_divisors(n: int) -> List[int]:
    divisors = []
    is_prime = False
    while not is_prime:
        i = first_divisor(n)
        if i == n:
            is_prime = True
        else:
            n = n // i
        divisors.append(i)
    return divisors


def find_common_divisors(a: List[int], b: List[int]) -> List[int]:
    a.sort()
    b.sort()
    common_divisors = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            common_divisors.append(a[i])
            i += 1
            j += 1
        else:
            if b[j] < a[i]:
                j += 1
            else:
                i += 1
    return common_divisors


#      B     D
# A + --- = ---
#      C     E
def sum_fraction(a: int, b: int, c: int) -> Tuple[int, int]:
    def _simplify(num: int, den: int) -> Tuple[int, int]:
        num_divisors = find_divisors(num)
        num_denominator = find_divisors(den)
        common_divisors = find_common_divisors(num_divisors, num_denominator)
        for d in common_divisors:
            num = num // d
            den = den // d
        return num, den

    numerator = a * c + b
    denominator = c
    # d, e = _simplify(numerator, denominator)  # not necessary
    d, e = numerator, denominator
    return d, e


def find_n_decimals_of_e(n: int) -> List[int]:
    mult_of_3 = n // 3
    remainder = n % 3
    decimals = []
    for i in range(1, mult_of_3 + 1):
        decimals.extend((1, 2 * i, 1))
    if remainder == 1:
        decimals.append(1)
    elif remainder == 2:
        decimals.extend((1, 2 * (mult_of_3 + 1)))
    return decimals


if __name__ == '__main__':

    n_convergents = 100
    integer_part = 2
    decimals = find_n_decimals_of_e(n_convergents - 1)
    if len(decimals) == 1:
        num, den = 2, 1
        print(f"{integer_part}")
    else:
        b = 1
        c = decimals[-1]
        for a in decimals[-2::-1]:
            d, e = sum_fraction(a, b, c)
            b = e
            c = d
        num, den = sum_fraction(integer_part, b, c)
    print(f"{num}/{den}, summation of numerator digits: {sum([int(i) for i in str(num)])}")

