import functools
import operator
import math

def isprime(n):
    if n != 1:
        for i in range(2, round(math.sqrt(n)) + 1):
            if n % i == 0 and i != n:
                return False
        return True
    else:
        return True


def factors(n1):
    
    # e.g. f = factors(600851475143)
    
    n2 = n1
    f = []
    a = 2

    while functools.reduce(operator.mul, f, 1) != n1: # finché la produttoria di 'f' non eguaglia 'n1'
        if n2 % a == 0:
            if isprime(a):
                while n2 % a == 0:
                    f.append(a)
                    #print('Found ' + str(a))
                    n2 = n2 / a
        a = a + 1
        #print('Test: ' + str(a) + '\n')

    #print(f)
    return f

