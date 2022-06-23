import functools
import operator
import math

def isprime(n):
    if n > 1:
        for i in range(2, round(math.sqrt(n)) + 1):
            if n % i == 0 and i != n:
                return False
        return True
    else:
        return False


def factors(n1):

    n2 = n1
    f = {}
    a = 2

    while functools.reduce(operator.mul, f, 1) != n1: # finché la produttoria di 'f' non eguaglia 'n1'
        if n2 % a == 0:
            if isprime(a):
                while n2 % a == 0:
                    if a in f:
                        f[a] += 1
                    else:
                        f[a] = 1
                    n2 = n2 // a
        if a < n2 / a:
            a = a + 1
        else:
             if len(f) > 0 and n2 != 1:
                 f[n2] = 1
             return f
    return f

def intersection(D1, D2):
    for k in D1:
        if k in D2:
            if D1[k] == D2[k]:
                return True
    return False

found = False
n = 2 * 3 * 5 * 7 
while not found:
    F1 = factors(n)
    #print('F1 = ', F1)
    if len(F1) == 4:
        F2 = factors(n + 1)
        #print('F2 = ', F2)
        if len(F2) == 4:
            # Check intersection
            if intersection(F1, F2) == False:
                F3 = factors(n + 2)
                if len(F3) == 4:
                    if intersection(F1, F3) == False and intersection(F2, F3) == False:
                        F4 = factors(n + 3)    
                        if len(F4) == 4:
                            print('n = ', n, 'F1 = ', F1, 'F2 = ', F2, 'F3 = ', F3, 'F4 = ', F4)
    
                            if intersection(F1, F4) == False and intersection(F2, F4) == False and intersection(F3, F4) == False:
                                found = True
                                print('First number is ' + str(n))
                            elif intersection(F3, F4) == True:
                                n += 3
                            elif intersection(F2, F4) == True:
                                n += 2
                            else:
                                n += 1
                        else:
                            n += 4
                    elif intersection(F2, F3) == True:
                        n += 2
                    else:
                        n += 1
                else:
                    n += 3
            else:
                n += 1
        else:
            n += 2
    else:
        n += 1
