d = 0 # divisors
n = 1
x = 1

while d < 500:
    
    n += 1
    x += n
    d = 0

    p = 1 # 1st divisor
    q = x # 1st quotient

    while p < q:
        if x % p == 0:
            q = x // p
            d += 2
        p += 1

print(x)

