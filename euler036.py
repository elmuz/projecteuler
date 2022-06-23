def palindromic_str(s):
    for i in range(len(s)//2):
        if s[i] != s[-i - 1]:
            return False
    return True

counter = 0
for i in range(1,1000000):
    if palindromic_str(str(i)) and palindromic_str("{0:b}".format(i)):
        counter += i

print(counter)
