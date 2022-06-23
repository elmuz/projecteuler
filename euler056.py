def digit_sum(n):
    l = list(str(n))
    return sum(map(int, l))

greatest = 0
for a in range(2, 100):
    for b in range(2, 100):
        if digit_sum(a ** b) > greatest:
            greatest = digit_sum(a ** b)
print(greatest)
