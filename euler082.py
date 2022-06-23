from typing import List

with open("p082_matrix.txt") as infile:
    matrix = infile.readlines()
matrix = [
    [
        int(n.strip())
        for n in line.split(",")
    ]
    for line in matrix
]

def pretty_print(matrix: List[List[int]]) -> None:
    for line in matrix:
        print(line)

def find_min_sum_path(matrix: List[List[int]]) -> int:
    best_path = 1000000
    row_max = len(matrix) - 1
    col_max = len(matrix[0]) - 1
    for row_start in range(len(matrix)):
        visited = [
            [
                False for _ in line
            ]
            for line in matrix
        ]
        best_sum = [
            [
                float("Inf") for _ in line
            ]
            for line in matrix
        ]
        to_check = [(row_start, 0)]
        visited[row_start][0] = True
        best_sum[row_start][0] = matrix[row_start][0]
        while len(to_check) > 0:
            row, col = to_check.pop(0)
            if col == col_max:
                continue
            # Check on the left
            # if col > 0:
            #     if visited[row][col - 1] is False or best_sum[row][col - 1] > best_sum[row][col] + matrix[row][col - 1]:
            #         best_sum[row][col - 1] = best_sum[row][col] + matrix[row][col - 1]
            #         visited[row][col - 1] = True
            #         to_check.append((row, col - 1))
            # Check on top
            if row > 0:
                if visited[row - 1][col] is False or best_sum[row - 1][col] > best_sum[row][col] + matrix[row - 1][col]:
                    best_sum[row - 1][col] = best_sum[row][col] + matrix[row - 1][col]
                    visited[row - 1][col] = True
                    to_check.append((row - 1, col))
            #Check on the right
            if col < col_max:
                if visited[row][col + 1] is False or best_sum[row][col + 1] > best_sum[row][col] + matrix[row][col + 1]:
                    best_sum[row][col + 1] = best_sum[row][col] + matrix[row][col + 1]
                    visited[row][col + 1] = True
                    to_check.append((row, col + 1))
            # Check on bottom
            if row < row_max:
                if visited[row + 1][col] is False or best_sum[row + 1][col] > best_sum[row][col] + matrix[row + 1][col]:
                    best_sum[row + 1][col] = best_sum[row][col] + matrix[row + 1][col]
                    visited[row + 1][col] = True
                    to_check.append((row + 1, col))
        for row in range(len(matrix)):
            if best_sum[row][col_max] < best_path:
                best_path = best_sum[row][col_max]
    return best_path


test_matrix = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331]
]
assert find_min_sum_path(test_matrix) == 994
print(find_min_sum_path(matrix))

