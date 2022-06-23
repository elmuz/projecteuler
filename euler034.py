def factorial(n):
    if n < 0:
        exit(1)
    elif n == 0:
        return 1
    return n * factorial(n - 1)

x = []
for i in range(10):
    x.append(factorial(i))

for i in range(3,1000000):
    s = 0
    for j in range(len(str(i))):
        s += x[int(str(i)[j])]
    if s == i:
        print(i)

# Is there a better way to know that it's gonna stop at 40585?
