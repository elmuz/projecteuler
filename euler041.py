import math
import itertools

def isprime(n):
    if n > 1:
        for i in range(2, math.floor(math.sqrt(n)) + 1):
            if n % i == 0 and i != n:
                return False
        return True
    else:
        return False

def ispalindromic(n):
    l = len(str(n))
    i = 0
    while i < l:
        if str(i + 1) not in str(n):
            return False
        else:
            i += 1
    return True

max_n = 0

# Generate palindromic numbers and then check if it is prime
"""
for n in range(987654321, 1, -1):
    if ispalindromic(n):
        if isprime(n):
            max_n = n
            break
"""
def largestPandigitalPrime():
    for digits in range(9, 1, -1):
        perms = list(itertools.permutations(range(1, digits + 1)))
        for i in reversed(perms):
            n = int(''.join(map(str, list(i)))) 
            if isprime(n):
                print(n)
                return

largestPandigitalPrime()
