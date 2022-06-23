import math
from typing import Tuple


def has_odd_period(radicand: int) -> bool:

    # Each fraction can be written as:
    #     sqrt(A) + B
    # D + -----------
    #          C
    def _sub_fraction(a_0: int, b_0: int, c_0: int) -> Tuple[int, int, int]:
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

    decimals = []
    remainders = []

    integer_part = int(math.sqrt(radicand))
    a_0 = radicand
    b_0 = -integer_part
    c_0 = 1

    found_period = False
    while not found_period:
        d_1, b_0, c_0 = _sub_fraction(a_0, b_0, c_0)
        if (b_0, c_0) in remainders:
            found_period = True
        else:
            decimals.append(d_1)
        remainders.append((b_0, c_0))

    if len(decimals) % 2 == 0:
        return False
    else:
        return True


def is_continued_fraction(n: int) -> bool:
    if int(math.sqrt(n)) ** 2 == n:
        return False
    else:
        return True

counter = 0
limit = 10000
for n in range(2, limit + 1):
    if is_continued_fraction(n):
        if has_odd_period(n):
            counter += 1

print(f"We found {counter} continued fraction(s) less or equal to sqrt({limit}) with odd period")