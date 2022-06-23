import math

def sumfactors(n):
    s = 1
    for i in range(2, int(math.floor(math.sqrt(n))) + 1):
        if n % i == 0:
            s = s + i
            if i != (n // i):
                s = s + (n // i)
                # print(str(i) + ',' + str(n // i))
            #else:
                # print(str(i) + '[x2]')
    return s

n = list(range(10000))
total_sum = 0
for i in n:
    if n[i] != 0:
        a = sumfactors(n[i])
        if a < 10000:
            b = sumfactors(a)
            if b == n[i] and a != n[i]:
                # They're amicable numbers!
                print(str(n[i]) + ' and ' + str(a) + ' are amicable!')
                total_sum = total_sum + a + n[i]
                n[a] = 0

print('Total sum: ' + str(total_sum))


