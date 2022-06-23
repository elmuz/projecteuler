import itertools

total = 0
for p in itertools.permutations(range(10)):
    n = ''.join(map(str, list(p)))
    if int(n[7:10]) % 17 != 0:
        continue
    elif int(n[6:9]) % 13 != 0:
        continue
    elif int(n[5:8]) % 11 != 0:
        continue
    elif int(n[4:7]) % 7 != 0:
        continue
    elif int(n[3:6]) % 5 != 0:
        continue
    elif int(n[2:5]) % 3 != 0:
        continue
    elif int(n[1:4]) % 2 != 0:
        continue
    else:
        print(n)
        total += int(n)

print('Total: ' + str(total))


