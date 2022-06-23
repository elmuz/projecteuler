def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


N = str(factorial(100))

S = 0

for i in range(len(N)):
    S += int(N[i])

print(S)
