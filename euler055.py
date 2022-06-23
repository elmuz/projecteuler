def is_palindromic(n):
    s = str(n)
    if s[::-1] == s:
        return True
    else:
        return False

def reverse_and_add(n):
    asdasd

lyrchel = 0
for n in range(1, 10000):
    it = 0
    is_lyrchel = True
    while it < 50:
        if is_palindromic(n + int(str(n)[::-1])):
            is_lyrchel = False
            break
        else:
            n += int(str(n)[::-1])
        it += 1
    if is_lyrchel:
        lyrchel += 1

print(lyrchel)
