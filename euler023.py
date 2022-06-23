import math

def sumfactors(n):
    s = 1
    for i in range(2, int(math.floor(math.sqrt(n))) + 1):
        if n % i == 0:
            s = s + i
            if i != (n // i):
                s = s + (n // i)
                #print(str(i) + ',' + str(n // i))
            #else:
                #print(str(i) + '[x2]')
    #print(str(n) + ', ' + str(s))
    return s

limit = 28123
ab = []

for i in range(2, limit + 1):
    if i < sumfactors(i):
        ab.append(i)
        #print(i)


N = list(range(limit + 1))
for i in range(len(ab)):
    for j in range(i, len(ab)):
        if ab[i] + ab[j] <= limit:
            N[ab[i] + ab[j]] = 0
            #print(ab[i] + ab[j])
        else:
            break
print(sum(N))
"""
total = 0
for n in range(limit + 1):
    for i in range(len(ab)):
        if ab[i] < n:
            if n - ab[i] in ab:
                break
        else:
            total += n
            print(n)
            break

print(total)
"""
