def sameDigits(x, y):
    x = list(str(x))
    y = list(str(y))
    if len(x) != len(y):
        return False
    else:
        for i in x:
            if i in y:
                y.remove(i)
            else:
                return False
        return True

found = False
i = 1
while not found:
    i6 = i * 6
    if sameDigits(i, i6):
        i5 = i * 5
        if sameDigits(i, i5):
            i4 = i * 4
            if sameDigits(i, i4):
                i3 = i * 3
                if sameDigits(i, i3):
                    i2 = i * 2
                    if sameDigits(i, i2):
                        found = True
                    else:
                        i += 1
                else:
                    i += 1
            else:
                i += 1
        else:
            i += 1
    else:
        i += 1
print(i)
