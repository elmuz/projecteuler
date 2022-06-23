
d = 0 # digits
i = 2 # index
n_1 = 1
n_2 = 1

while d < 1000:
    i += 1
    n = n_1 + n_2
    n_2 = n_1
    n_1 = n
    d = len(str(n))
print(i)

