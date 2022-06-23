import numpy as np

c = np.empty(1001, dtype=np.int) # from 0 to 1000
W = 1001 * ['']

l1 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
l2 = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
l3 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
h = 'hundred'
k = 'thousand'

for i in range(len(l1)):
    c[i] = len(l1[i])
    c[10 + i] = len(l2[i])
    W[i] = l1[i]
    W[10 + i] = l2[i]

for i in range(len(l3)):
    c[10 + 10 * (i + 1)] = len(l3[i])
    W[10 + 10 * (i + 1)] = l3[i]

c[100] = len(h)
c[1000] = len(k)
W[100] = h
W[1000] = k

def counter(n):
    s = 0
    w = ''
    if len(str(n)) >= 4:
        s = s + c[int(str(n)[-4])] + c[1000]
        w = w + W[int(str(n)[-4])] + W[1000]
    if len(str(n)) >= 3:
        if int(str(n)[-3]) != 0:
            s = s + c[int(str(n)[-3])] + c[100]
            w = w + W[int(str(n)[-3])] + W[100]
        if int(str(n)[-2]) != 0 or int(str(n)[-1]) != 0:
            s = s + 3
            w = w + 'and'
    if len(str(n)) >= 2:
        if int(str(n)[-2]) == 1:
            s = s + c[int(str(n)[-2:])]
            w = w + W[int(str(n)[-2:])]
            print(str(w) + ',' + str(s))
            return s
        elif int(str(n)[-2]) != 0:
            s = s + c[int(str(n)[-2]) * 10]
            w = w + W[int(str(n)[-2]) * 10]
    if len(str(n)) >= 1:
        s = s + c[int(str(n)[-1])]
        w = w + W[int(str(n)[-1])]
    print(str(w) + ',' + str(s))
    return s

total = 0

for i in range(1,1001):
    total = total + counter(i)

print(total)
