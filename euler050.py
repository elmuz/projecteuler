import math

def isprime(n):
    if n > 1:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0 and i != n:
                return False
        return True
    else:
        return False

def addNextPrime(primes, last):
    n = last + 1
    while not isprime(n):
        n += 1
    primes.append(n)
    return primes, n

print('Looking for sum of primes')
primes = [2]
last_prime = 2
n = 1000000
upprimes = []
longest = 0
# Look for the almost optimal solution
foundSum = False
while not foundSum:
    if isprime(n):
        upprimes.append(n)
        sumOfPrimes = sum(primes)
        while sumOfPrimes < n:
            primes, last_prime = addNextPrime(primes, last_prime)
            sumOfPrimes += primes[-1]
        # No need to look for more primes
        partial = 0
        i = 0
        while partial < n:
            partial += primes[i]
            i += 1
        if partial == n:
            foundSum = True
            longest = i
        else:
            n -= 1
    else:
        n -= 1
sub_primes = primes[:longest]
best = len(sub_primes)
print('Sub-optimal solution',n,'with',len(sub_primes),'primes (',sub_primes[0],'...',sub_primes[-1],')')
#print(sum(sub_primes))
# Look for optimal solution
for n in upprimes[0:-1]:
    last_sequence = best + 1
    offset = 1
    while last_sequence > best:
        shift_primes = sub_primes[offset:]
        last_temp = sub_primes[-1]
        #print(sum(shift_primes))
        while sum(shift_primes) < n:
            shift_primes, last_temp = addNextPrime(shift_primes, last_temp)
        last_sequence = len(shift_primes)
        #print(n,shift_primes[0],shift_primes[-1],len(shift_primes))
        if sum(shift_primes) == n:
            best = len(shift_primes)
            print('Better solution:',n,'with',best,'primes (',shift_primes[0],'...',shift_primes[-1],')')
        else:
            offset += 1

