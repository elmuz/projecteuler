from typing import List, Tuple


with open("p079_keylog.txt") as infile:
    keys = infile.readlines()
keys = [k.strip() for k in keys]

def is_legit_triple(n: int, key: str) -> bool:
    n_str = str(n)
    i_start = 0
    for s in key:
        found = False
        for i, n_i in enumerate(n_str[i_start:]):
            if n_i == s:
                i_start += i + 1
                found = True
                break
        if not found:
            return False
    return True

assert is_legit_triple(123456, "134")
assert is_legit_triple(123456, "456")
assert is_legit_triple(123456, "356")
assert is_legit_triple(1234561, "351")
assert not is_legit_triple(123456, "566")
assert not is_legit_triple(123456, "321")


def overlap(str_1: str, str_2: str) -> int:
    if len(str_1) < len(str_2):
        k_1 = str_1
        k_2 = str_2
    else:
        k_1 = str_2
        k_2 = str_1

    max_counter = 0

    for k in range(len(k_1)):
        i_1 = k
        i_2 = 0
        last_match = -1
        counter = 0
        while i_1 < len(k_1):
            if k_1[i_1] == k_2[i_2]:
                counter += 1
                last_match = i_2
                i_1 += 1
                i_2 += 1
            else:
                i_2 += 1
            if i_2 == len(k_2):
                if i_1 == len(k_1) - 1:
                    break
                else:
                    i_1 += 1
                    i_2 = last_match
        if counter > max_counter:
            max_counter = counter
    return max_counter

assert overlap("123", "234") == 2
assert overlap("123", "321") == 1
assert overlap("123", "345") == 1
assert overlap("123", "445") == 0
assert overlap("111", "112") == 2
assert overlap("112", "112") == 3
assert overlap("112", "102") == 2
assert overlap("112", "101") == 2
assert overlap("123", "231") == 2
assert overlap("123", "123123") == 3
assert overlap("123123", "123") == 3
assert overlap("10203", "123") == 3
assert overlap("123", "10203") == 3
assert overlap("123", "00100") == 1
assert overlap("321", "30102") == 2


def sorted_pairs(keys: List[str]) -> List[Tuple[int, str, int, str, int]]:
    mutual_overlap = []
    for i, k_i in enumerate(keys):
        for j in range(i + 1, len(keys)):
            k_j = keys[j]
            mutual_overlap.append((i, k_i, j, k_j, overlap(k_i, k_j)))
    return sorted(mutual_overlap, key=lambda x: x[4], reverse=True)


output = ""
while len(keys) > 0:
    mutual_overlap = sorted_pairs(keys)
    i, k_i, j, k_j, m = mutual_overlap.pop(0)
    merged = merge(k_i, k_j)
    keys = [k for k in keys if k not in [k_i, k_j]]
