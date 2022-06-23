FACTORIALS = {0: 1, 1: 1}
def fact(n: int) -> int:
    if n < 0:
        raise ValueError
    if n in FACTORIALS:
        return FACTORIALS[n]
    else:
        result = n * fact(n - 1)
        FACTORIALS[n] = result
        return result

