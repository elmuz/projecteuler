import math
from itertools import product


def compute_partitions(n_digits):
    partitions = []
    for seq in product(range(2), repeat=n_digits - 1):
        if sum(seq) == 0:
            continue

        next_seq = False
        
        s = [0] + list(seq)
        indices = []
        placeholder = 0
        for j in range(1, n_digits):
            if next_seq:
                break
            if s[j] != s[j - 1]:
                if j - placeholder > math.ceil(n_digits / 2):
                    next_seq = True
                    break
                indices.append((placeholder, j))
                placeholder = j
        indices.append((placeholder, n_digits))
        sorted(indices, key=lambda i: i[1] - i[0], reverse=True)
        partitions.append(indices)
    return partitions


def T(N):
    total = 0
    partitions = {}
    for i in range(int(math.sqrt(N)) + 1):

        i2 = i ** 2
        i2_str = str(i2)

        n_digits = len(i2_str)

        if n_digits not in partitions:
            partitions[n_digits] = compute_partitions(n_digits)

        for partition in partitions[n_digits]:
            partial = 0
            for indices in partition:
                partial += int(i2_str[indices[0]:indices[1]])
                if partial > i:
                    break
            if partial == i:
                total += i2
                print(i, i2, partition)
                break
    return total


print(f"T(1e12): {T(int(1e12))}")
