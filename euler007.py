from euler003 import isprime

c = 0
i = 0
while c <= 10001:
    i += 1
    if isprime(i):
        c += 1

print(i)

