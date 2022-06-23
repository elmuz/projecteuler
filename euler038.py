def isunique(n):
    if len("".join(set(n))) == len(n):
        return True
    else:
        return False

max_concat = 123456789

for i in range(1,9999):
    concat = ''
    n = 1
    unique = True
    while len(concat) < 9:
        concat += str(i * n)
        if not isunique(concat):
            unique = False
            break
        n += 1
    if not unique: # 9 or 10 digits, with or w/o the 0
        continue
    elif concat.find('0') == -1 and len(concat) == 9:
        print('(' + str(i) + ',' + str(n -1) + '): ' + concat)
        if int(concat) > max_concat:
            max_concat = int(concat)

print(max_concat)
