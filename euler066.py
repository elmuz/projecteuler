"""
Quadratic Diophantine equation
x ** 2 - D * y ** 2 = 1

"""

import math
from typing import List, Tuple


def find_next_convergent(a_n: int, h_n_1: int, h_n_2: int, k_n_1: int, k_n_2: int) -> Tuple[int, int]:
    # See https://en.wikipedia.org/wiki/Continued_fraction
    h_n = a_n * h_n_1 + h_n_2
    k_n = a_n * k_n_1 + k_n_2
    return h_n, k_n


def find_next_fraction(a_0: int, b_0: int, c_0: int) -> Tuple[int, int, int]:
    """
    Each fraction can be written as:
        sqrt(A) + B
    D + -----------
             C
    """
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


def solve_diophantine_eq(D: int) -> Tuple[int, int, int]:
    # See https://en.wikipedia.org/wiki/Pell%27s_equation
    h_n = None
    h_n_1 = 1
    h_n_2 = 0
    k_n = None
    k_n_1 = 0
    k_n_2 = 1

    found_solution = False
    a_n = math.isqrt(D)
    b_n_1 = -math.isqrt(D)
    c_n_1 = 1
    while not found_solution:
        h_n, k_n = find_next_convergent(a_n, h_n_1, h_n_2, k_n_1, k_n_2)
        a_n, b_n, c_n = find_next_fraction(D, b_n_1, c_n_1)
        b_n_1 = b_n
        c_n_1 = c_n

        # Check Diophantine equation
        if h_n ** 2 - D * k_n ** 2 == 1:
            found_solution = True
            print(f"{D}: {h_n}^2 - {D} * {k_n}^2 = 1")

        h_n_2 = h_n_1
        h_n_1 = h_n
        k_n_2 = k_n_1
        k_n_1 = k_n

    return h_n, k_n, D


if __name__ == '__main__':

    max_x = 0
    y_ = 0
    D_ = 0

    limit = 1000
    results = []
    for D in range(2, limit + 1):
        if math.isqrt(D) ** 2 != D:
            results.append(solve_diophantine_eq(D))
    for x, y, D in results:
        if x > max_x:
            max_x = x
            y_ = y
            D_ = D

    print(f"The D that brings the highest `x` is {D_}: {max_x}^2 - {D_} * {y_}^2 = 1")