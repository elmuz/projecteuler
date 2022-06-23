import math
from decimal import *
from typing import List

getcontext().prec = 200

def compute_sqrt(r: int, decimals: int) -> List[int]:
    s = str(Decimal(r).sqrt()).replace(".", "")[:decimals]
    i = [int(c) for c in s]
    return i

assert compute_sqrt(91, decimals=4) == [9, 5, 3, 9]
assert sum(compute_sqrt(2, decimals=100)) == 475


def has_irrational_sqrt(n: int) -> bool:
    if math.isqrt(n) ** 2 == n:
        return False
    else:
        return True

assert has_irrational_sqrt(2)
assert has_irrational_sqrt(3)
assert not has_irrational_sqrt(4)
assert has_irrational_sqrt(5)
assert has_irrational_sqrt(6)
assert has_irrational_sqrt(7)
assert has_irrational_sqrt(8)
assert not has_irrational_sqrt(9)


if __name__ == '__main__':
    total = 0
    for i in range(1, 100 + 1):
        if has_irrational_sqrt(i):
            total += sum(compute_sqrt(i, decimals=100))
    print(f"Total amount is: {total}.")