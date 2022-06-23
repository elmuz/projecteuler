import math
from itertools import combinations, islice


def is_permutation(i: int, j: int) -> bool:
    if int(math.log10(i)) != int(math.log10(j)):
        return False

    j_str = str(j)
    for c in str(i):
        idx = j_str.find(c)
        if idx >= 0:
            j_str = j_str[:idx] + j_str[idx+ 1:]
        else:
            return False

    return True

n = 1  # leverage problem description
found = False
length = int(math.log10(n ** 3))
cubes = {n ** 3: []}
while not found:

    n += 1
    new = n ** 3
    if int(math.log10(new)) > length:
        cubes = {new: []}
        length = int(math.log10(new))
    else:
        for cube_key, cube_list in cubes.items():
            if is_permutation(cube_key, new):
                if len(cube_list) == 3:
                    found = True
                    print("Found!", cube_key, cube_list, new)
                    break
                cubes[cube_key].append(new)
        cubes[new] = []