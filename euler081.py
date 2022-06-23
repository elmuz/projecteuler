from typing import List

with open("p081_matrix.txt") as infile:
    matrix = infile.readlines()
matrix = [
    [
        int(n.strip())
        for n in line.split(",")
    ]
    for line in matrix
]

def update_min(matrix: List[List[int]], row: int, col: int) -> None:
    if row == 0:
        up = float("Inf")
    else:
        up = matrix[row - 1][col]
    if col == 0:
        left = float("Inf")
    else:
        left = matrix[row][col - 1]
    matrix[row][col] = matrix[row][col] + min(up, left)


def find_min_sum_path(matrix: List[List[int]]) -> int:
    for vert_diag in range(1, len(matrix)):
        for i in range(vert_diag + 1):
            update_min(matrix, vert_diag - i, i)
    for horiz_diag in range(len(matrix) - 1, 0, -1):
        for i in range(horiz_diag):
            update_min(matrix, len(matrix) - i - 1, len(matrix) - horiz_diag  + i)
    return matrix[-1][-1]


test_matrix = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331]
]
assert find_min_sum_path(test_matrix) == 2427
print(find_min_sum_path(matrix))

