if __name__ == '__main__':
    partial_sums = []
    with open("/p067_triangle.txt") as input_file:
        lines = input_file.readlines()

    for line in lines[::-1]:
        values = line.strip("\n").split()
        if len(partial_sums) == 0:
            partial_sums = [int(v) for v in values]
            continue
        new_sums = []
        for idx, v in enumerate(values):
            left_idx = idx
            right_idx = idx + 1
            new_sums.append(int(v) + max(partial_sums[left_idx], partial_sums[right_idx]))
        partial_sums = new_sums
    print(partial_sums)