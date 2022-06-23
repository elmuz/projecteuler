a = []
p = 5

# Find limit
limit = True
d = 1
while limit == True:
    length = d * (9 ** p)
    if length < 10 ** d:
        limit = False
    else:
        d += 1

print('Limit: ' + str(d))

for i in range(2,10**d):
    s = 0
    for n in range(len(str(i))):
        s = s + int(str(i)[n])**5
    if s == i:
        print(i)
        a.append(i)

print('Somma: ' + str(sum(a)))
