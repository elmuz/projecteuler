from euler003 import isprime

s = 0
for i in range(2,2000000):
    if isprime(i):
        s = s + i
print(s)

