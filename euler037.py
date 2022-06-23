import math

def isprime(n):
    if n > 1:
        for i in range(2, math.floor(math.sqrt(n)) + 1):
            if n % i == 0 and i != n:
                return False
        return True
    else:
        return False

counter = 0
total_sum = 0
n = 11
while counter < 11:
    trunc_prime = True
    for i in range(len(str(n))):
        if not isprime(int(str(n)[0:i + 1])):
            trunc_prime = False
            break
        elif not isprime(int(str(n)[len(str(n)) - 1 - i:len(str(n))])):
            trunc_prime = False
            break
    if trunc_prime:
        print(n)
        total_sum += n
        counter += 1
    n += 1

print('Sum: ' + str(total_sum))
