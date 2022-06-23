def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    """
    Idea: most common divisors are lowest primes. Given two primes the
    lower has more chances to appear as a divisor of greater numbers.
    Therefore:
    1) look for the number M <= 1e6 which contains most prime divisors.
    2) Inspect all numbers from M's greatest divisor up to M - 1. If
       they do not have common divisors they are coprimes with M.
    3) Return the ratio between M and the number of coprimes.
    """

    prod = 2
    i = 2
    primes = [2]
    coprimes = [1]
    while prod <= 1000000:
        i += 1
        if is_prime(i):
            primes.append(i)
            prod *= i
    prod = prod // primes[-1]
    primes.pop()
    print(f"Our number M is {prod}, which is the product of {primes}")
    for i in range(primes[-1] + 1, prod):
        valid_number = True
        for j in primes:
            if i % j == 0:
                valid_number = False
                break
        if valid_number:
            coprimes.append(i)
    print(f"There are {len(coprimes)} coprimes with M from {primes[-1] + 1} and (M-1).")
    print(f"Coprimes: [{coprimes[0]}, {coprimes[1]}, ... , {coprimes[-2]}, {coprimes[-1]}]")
    print(f"Max ratio: {prod / len(coprimes):.3f}")

