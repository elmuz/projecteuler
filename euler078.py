"""
This function takes space complexity too high
"""
LOOKUP = {0: {}}
def find_combo(n: int) -> int:
    # This function must be called sequentially
    assert n <= max(LOOKUP.keys()) + 1

    counter = 0
    lookup_n = {}
    for i in range(1, n):
        if i >= n - i:
            counter += LOOKUP[n - i]["tot"]
            lookup_n[i] = LOOKUP[n - i]["tot"]
        else:
            counter += LOOKUP[n - i]["up_to_" + str(i)]
            lookup_n[i] = LOOKUP[n - i]["up_to_" + str(i)]
        lookup_n["up_to_" + str(i)] = counter
    counter += 1
    lookup_n[n] = 1
    lookup_n["tot"] = counter
    LOOKUP[n] = lookup_n
    return counter

assert find_combo(1) == 1
assert find_combo(2) == 2
assert find_combo(3) == 3
assert find_combo(4) == 5
assert find_combo(5) == 7
assert find_combo(6) == 11
assert find_combo(7) == 15

"""
See this for an explanation
https://brilliant.org/wiki/partition-of-an-integer/
"""
PARTITIONS_LIST = {0: 1}
PENTAGONALS = {}
def find_combo_smart(n: int) -> int:
    def _penta(p: int) -> int:
        if p in PENTAGONALS:
            return PENTAGONALS[p]
        else:
            PENTAGONALS[p] = p * (3 * p - 1) // 2
            return PENTAGONALS[p]

    if n < 0:
        return 0

    i = 0
    j = 1
    penta = _penta(j)
    counter = 0
    while penta <= n:
        if i % 4 < 2:
            sign = 1
        else:
            sign = -1
        counter += sign * PARTITIONS_LIST[n - penta]
        if j < 0:
            j = -j + 1
        else:
            j = -j
        penta = _penta(j)
        i += 1
    PARTITIONS_LIST[n] = counter
    return counter

assert find_combo_smart(1) == 1
assert find_combo_smart(2) == 2
assert find_combo_smart(3) == 3
assert find_combo_smart(4) == 5
assert find_combo_smart(5) == 7
assert find_combo_smart(6) == 11
assert find_combo_smart(7) == 15

found = False
n = 1
while not found:
    counter = find_combo_smart(n)
    if counter % 1000000 == 0:
        print(f"Found! n: {n}, counter:{counter}")
        break
    else:
        print(n, counter)
        n += 1

