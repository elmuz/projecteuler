# Given numerical days where:
# n == 0: Monday
# n == 1: Tuesday
# ...
# n == 6: Sunday

def is_leap(n):
    if n % 400 == 0:
        return 1
    elif n % 100 == 0:
        return 0
    elif n % 4 == 0:
        return 1
    else:
        return 0

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

counter = 0
d = 0 # Jan 1st 1900 was a Monday
for y in range(1900,2001):
    months[1] = 28 + is_leap(y)
    for m in range(12): 
        if d == 6 and y > 1900:
            counter += 1
        d = (d + months[m]) % 7
        
print(counter)
