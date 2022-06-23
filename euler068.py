"""
Let's refer to these index-position relation:
            0
              \
                1        3
            *       *   /
        8              2
     /   \            /
  9       \          /
           6 ------- 4 ---- 5
             \
              7
"""

import itertools
from typing import List


def is_valid_order(sequence: List[int]) -> bool:
    if sequence[0] == min([sequence[0], sequence[3], sequence[5], sequence[7], sequence[9]]):
        return True
    else:
        return False


def is_valid_pentagon_ring(sequence: List[int]) -> bool:
    assert sorted(sequence) == list(range(1, 11))

    indices = [
        [0, 1, 2],
        [3, 2, 4],
        [5, 4, 6],
        [7, 6, 8],
        [9, 8, 1]
    ]
    i, j, k = indices[0]
    total = sequence[i] + sequence[j] + sequence[k]
    for i, j, k in indices[1:]:
        total_new = sequence[i] + sequence[j] + sequence[k]
        if total_new != total:
            return False
    return True


def full_reading_sequence(sequence: List[int]) -> List[int]:
    assert len(sequence) == 10
    return [sequence[i] for i in [0, 1, 2, 3, 2, 4, 5, 4, 6, 7, 6 ,8, 9, 8, 1]]


if __name__ == '__main__':
    best_sequence = 0
    for sequence in itertools.permutations(range(1, 11)):
        if is_valid_order(list(sequence)):
            if is_valid_pentagon_ring(list(sequence)):
                sequence_str = "".join(str(i) for i in full_reading_sequence(list(sequence)))
                if len(sequence_str) == 16:
                    if int(sequence_str) > best_sequence:
                        best_sequence = int(sequence_str)
    print(f"Greatest 16-digits valid sequence {best_sequence}")
