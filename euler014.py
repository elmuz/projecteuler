def next(n):
    if n % 2 == 0:
        return n // 2
    else:
        return n * 3 + 1

best_s = 0
length = 0

for i in range(1000000, 0, -1):
    
    n = i
    counter = 1
    while n != 1:
        n = next(n)
        counter += 1
    if counter > length:
        length = counter
        best_s = i

print(best_s)
print(length)

