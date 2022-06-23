import itertools
import math

def isprime(n):
    if n > 1:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0 and i != n:
                return False
        return True
    else:
        return False

def increment_not_star(n, idx):
    # Extract not-star digits and increment by 2
    a = ''
    for i in range(len(str(n))):
            if i in idx:
                a += str(n)[i]
    len_before = len(a)
    a = int(a)
    a += 2
    a = str(a).zfill(len_before)

    # Check if 999 -> 1001
    if len(a) > len_before:
        return -1

    # Then replace 'n' accordingly
    pos = 0
    n_new = ''
    for i in range(len(str(n))):
        if i in idx:
            n_new += a[pos]
            pos += 1
        else:
            n_new += str(n)[i]
    #print(n,idx,n_new)
    return int(n_new)

def init_star(n, idx):
    # If n[0] == * set all * to 1, otherwise set all * to 0
    n_new = ''
    for i in range(len(str(n))):
        if i in idx:
            if 0 in idx:
                n_new += '1'
            else:
                n_new += '0'
        else:
            n_new += str(n)[i]
    return int(n_new)


def increment_star(n, idx):
    # Check if * are already at 9
    star_value = str(n)[idx[0]]
    if star_value == '9':
        return -1
    else:
        star_value = str(int(star_value) + 1)
    n_new = ''
    for i in range(len(str(n))):
        if i in idx:
            n_new += star_value
        else:
            n_new += str(n)[i]
    #print(n,idx,n_new)
    return int(n_new)


e = 4
family = 0
while family < 8:
    base = 10 ** e + 1 # start checking from 1001, then 10001, ...
    n = base
    star_positions = len(str(n)) - 1
    for i in range(1, 2 ** star_positions):
        s = bin(i)[2:].zfill(star_positions)
        star_idx = []
        not_star_idx = []
        for j in range(len(s)):
            if s[j] == '0':
                not_star_idx.append(j)
            else:
                star_idx.append(j)
        not_star_idx.append(j + 1)
        #print(s,star_idx, not_star_idx)

        # Increment all non-* digits
        n = base
        while True:
            n = init_star(n, star_idx)
            #print(n, star_idx)
            family = 0
            not_family = 0

            while not_family < 3:                
                #print(star_idx,n,family)

                if isprime(n):
                    family += 1
                else:
                    not_family += 1
                if increment_star(n, star_idx) > 0:
                    n = increment_star(n, star_idx)
                else:
                    break

            #print(star_idx,n,family)
            if family == 8:
                print(init_star(n, star_idx))
                exit()
            
            if  increment_not_star(n, not_star_idx) > 0:
                n = increment_not_star(n, not_star_idx)
            else:
                break

    # Increment 'n'
    e += 1
 
