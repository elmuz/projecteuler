import math
import functools
import operator
from euler003 import factors

def isPalindromic(n):
    d = math.floor(math.log10(n)) + 1
    for i in range(d // 2):
        if ((n % 10**(i + 1)) // 10**i) != ((n % 10**(d - i)) // 10**(d - i - 1)):
            return False
    return True

"""
def nextLowerPalindromic(n):
    
    # Given 'n' is palindromic
    d = len(str(n))
    left = int(str(n)[:math.ceil(d / 2)])
    odd = d % 2
    if odd == 0:
        if len(str(left)) == len(str(left - 1)):
            return int(str(left - 1) + str(left - 1)[::-1])
        else:
            return int(str(left - 1) + '9' + str(left - 1)[::-1])
    else:
        if len(str(left)) == len(str(left - 1)):
            return int(str(left - 1) + str(left - 1)[len(str(left - 1))-2::-1])
        else:
            return int(str(left - 1) + str(left - 1)[::-1])

a = 1000*1000 # upper limit

while True:
    a = nextLowerPalindromic(a)
    f = factors(a)

    # This can be done a lot better
    if len(str(f[-1])) == 3:
        if len(str(functools.reduce(operator.mul, f[:-1], 1))) == 3:
            print(str(a) + ', [' + str(functools.reduce(operator.mul, f[:-1], 1)) + ',' + str(f[-1]) + ']')
            break
"""

c = 0
for a in range(100,1000):
    for b in range(100,1000):
        if isPalindromic(a*b):
            if a*b > c:
                c = a*b

print(c)



