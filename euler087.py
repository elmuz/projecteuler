import math

from primes import Primes


def run():
    my_numbers = []
    limit = 50000000
    highest_possible_prime = math.floor(limit ** 0.5)
    
    # Precompute all possible needed primes
    while Primes.prime_numbers[-1] < highest_possible_prime:
        Primes._add_next_prime()
    
    for a in Primes.prime_numbers:
        for b in Primes.prime_numbers:
            for c in Primes.prime_numbers:
                t = a ** 2 + b ** 3 + c ** 4
                if t < limit:
                    my_numbers.append(t)
                else:
                    break
    
    print(len(set(my_numbers)))


if __name__ == '__main__':
    run()