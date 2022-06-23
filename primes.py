import math
import random
import time
from typing import Iterable


class Primes:
    """
    These are latest performance results:
    Max N: 1e4, naive/bruteforce: 1.98 usec, lookup table/lazy: 2.52 usec
    Max N: 1e5, naive/bruteforce: 3.03 usec, lookup table/lazy: 3.30 usec
    Max N: 1e6, naive/bruteforce: 6.71 usec, lookup table/lazy: 6.12 usec
    Max N: 1e7, naive/bruteforce: 18.58 usec, lookup table/lazy: 14.54 usec

    """

    prime_numbers = [2, 3, 5]

    @classmethod
    def is_prime(cls, n: int, strategy: str = "lazy") -> bool:
        if strategy == "lazy":
            return cls._is_prime_lazy(n)
        elif strategy == "brute":
            return cls._is_prime_bruteforce(n)
        else:
            raise NotImplementedError
    
    @classmethod
    def _is_prime_lazy(cls, n: int) -> bool:
        if n < 2:
            return False
        if n in cls.prime_numbers:
            return True
        if n < cls.prime_numbers[-1]:
            return False

        # Look for possible divisors
        ubnd = math.floor(math.sqrt(n))
        if ubnd <= cls.prime_numbers[-1]:
            for prime in cls.prime_numbers:
                if prime > ubnd:
                    break  # it's a new prime!
                if n % prime == 0:
                    return False

            # [2, ..., `up_bnd`, ..., `last_known_prime`, ... `n`]
            # We need to feel the gap between `last_known_prime` and `n`.
            cls._look_for_primes_in_range(range(cls.prime_numbers[-1] + 1, n + 1))

            # Previous range included `n` too.
            if n in cls.prime_numbers:
                return True
            else:
                return False
        else:
            # Start by testing all known primes as possible divisors
            last_known_prime = cls.prime_numbers[-1]
            last_known_prime_idx = len(cls.prime_numbers)
            for prime in cls.prime_numbers:
                if n % prime == 0:
                    return False

            # [2, ..., `last_known_prime`, ..., `up_bnd`, ..., `n`]
            # Look for the remaining possible (primes) divisors in range
            # [`last_known_prime` + 1, ..., `up_bnd`]
            cls._look_for_primes_in_range(range(cls.prime_numbers[-1] + 1, ubnd + 1))

            # Look for divisors from [last_known_prime, ..., lowes_prime_of(up_bnd)]
            # FIXME: Here there's room for efficiency improvement.
            for prime in cls.prime_numbers[last_known_prime_idx:]:
                if n % prime == 0:
                    return False
            for maybe_prime in range(cls.prime_numbers[-1] + 1, ubnd + 1):
                if n % maybe_prime == 0:
                    return False
            return True

    @classmethod
    def _look_for_primes_in_range(cls, sequence: Iterable[int]) -> None:
        for n in sorted(sequence):
            # Check possible divisors between [2, ..., up_bnd]. Upper bound
            # should be much lower than last known prime.
            ubnd = math.floor(math.sqrt(n))
            if ubnd > cls.prime_numbers[-1]:
                raise NotImplementedError

            is_prime = False
            for prime in cls.prime_numbers:
                if prime > ubnd:
                    is_prime = True
                    break
                if n % prime == 0:
                    break
            if is_prime:
                cls.prime_numbers.append(n)
    
    @classmethod
    def _add_next_prime(cls) -> int:
        n_primes = len(cls.prime_numbers)
        m = 1
        while len(cls.prime_numbers) == n_primes:
            n = cls.prime_numbers[-1] + m
            if cls.is_prime(n):
                # It should already be part of the list at this point
                if cls.prime_numbers[-1] < n:
                    cls.prime_numbers.append(n)
            else:
                m += 1
        return cls.prime_numbers[-1]

    @staticmethod
    def _is_prime_bruteforce(n: int) -> bool:
        for i in range(2, int(n ** 0.5 + 1)):
            if n % i == 0:
                return False
        return True


def measure_prime_search(complexity: int, search_strategy: str) -> float:
    t_s = []
    sequence = list(range(int(10 ** complexity)))
    random.shuffle(sequence)
    for i in sequence:
        t_0 = time.time()
        Primes.is_prime(i, search_strategy)
        t_s.append(time.time() - t_0)
    return sum(t_s) / 10 ** complexity


if __name__ == "__main__":

    # primes = Primes()
    # if primes.is_prime(42643801, strategy="brute"):
    #     print(f"{42643801} is prime (brute force)")
    # else:
    #     print("Not prime")
    #
    # if primes.is_prime(42643801, strategy="lazy"):
    #     print(f"{42643801} is prime (lazy)")
    # else:
    #     print("Not prime")

    # Find all primes below 1M
    while len(Primes.prime_numbers) < 1000:
        print(Primes._add_next_prime())
