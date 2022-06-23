from itertools import combinations


class Primes:
    numbers = [2]
    valid_prime_pairs = {2: []}
    random_checked = {2: True}
    largest_prime = 2
    largest_checked = 2

    set_size = 5
    found_subset = False

    @classmethod
    def extend_primes(cls) -> int:
        i = 1
        while True:
            if cls.add_if_prime(cls.largest_checked + i):
                return cls.largest_prime
            else:
                i += 1

    # @classmethod
    # def check_group_of_primes(cls, group_of_five):
    #     for prime_i, prime_j in combinations(group_of_five, 2):
    #         if (prime_i, prime_j) in cls.prime_pairs:
    #             if not cls.prime_pairs[(prime_i, prime_j)]:
    #                 return False
    #         else:
    #             prime_ij = int(str(prime_i) + str(prime_j))
    #             prime_ji = int(str(prime_j) + str(prime_i))
    #             if not cls.is_prime(prime_ij):
    #                 return False
    #             if not cls.is_prime(prime_ji):
    #                 return False
    #
    #             cls.prime_pairs[(prime_i, prime_j)] = True
    #             cls.prime_pairs[(prime_j, prime_i)] = True
    #     return True
    @classmethod
    def check_new_prime(cls, new_prime):
        pass

    @classmethod
    def add_if_prime(cls, target: int) -> bool:
        """ Lazy method for prime search """
        if target in cls.random_checked:
            if target <= cls.largest_checked:  # Already processed number
                return cls.random_checked[target]
            else:
                if cls.random_checked[target]:
                    cls.update_internal_checks(target)
                    return True
                else:
                    return False
        else:
            for n in range(cls.largest_checked + 1, target + 1):
                new_prime = True
                for i in range(2, int(n ** 0.5 + 1)):
                    if n % i == 0:
                        new_prime = False
                        break
                if new_prime:
                    cls.random_checked[n] = True
                    cls.update_internal_checks(n)
                else:
                    cls.largest_checked = n
                    cls.random_checked[n] = False

            if target == cls.largest_prime:
                return True
            else:
                return False

    @classmethod
    def update_internal_checks(cls, n):
        cls.numbers.append(n)
        cls.largest_prime = n
        cls.largest_checked = n
        prime_j = n
        for prime_i, pairable_list in cls.valid_prime_pairs.items():
            join_ij = int(str(prime_i) + str(prime_j))
            join_ji = int(str(prime_j) + str(prime_i))
            if cls.is_prime(join_ij) and cls.is_prime(join_ji):

                # We found two valid primes for subset: `n` and `prime_i`

                for i, j, k in combinations(pairable_list, 3):

                    valid = True
                    if j in cls.valid_prime_pairs[i] and k in cls.valid_prime_pairs[i] and k in cls.valid_prime_pairs[
                        j]:

                        # Check those against n
                        prime_a = n
                        for prime_b in [i, j, k]:
                            if not valid:
                                break
                            join_ab = int(str(prime_a) + str(prime_b))
                            join_ba = int(str(prime_b) + str(prime_a))
                            if cls.is_prime(join_ab) and cls.is_prime(join_ba):
                                pass
                            else:
                                valid = False

                        if valid:
                            print("Found!", [prime_i, i, j, k, n])
                            print("Sum", sum([prime_i, i, j, k, n]))
                            cls.found_subset = True
                            return

                pairable_list.append(prime_j)
        cls.valid_prime_pairs[n] = []

    @classmethod
    def is_prime(cls, n):
        if n in cls.random_checked:
            return cls.random_checked[n]
        else:
            for i in range(2, int(n ** 0.5 + 1)):
                if n % i == 0:
                    cls.random_checked[n] = False
                    return False
            cls.random_checked[n] = True
            return True


target_size_of_set = 5
prime_pair_set = set()

# Warm-up
while len(Primes.numbers) < target_size_of_set:
    Primes.extend_primes()

print(f"Warm-up! These are the first 5 primes: {Primes.numbers}")

while not Primes.found_subset:
    # Add a new prime
    new_prime = Primes.extend_primes()
