numbers = []

base = 1
exp = 1

while len(str(9 ** exp)) >= exp:
    base = 1
    while len(str(base ** exp)) <= exp:
        if len(str(base ** exp)) == exp:
            numbers.append(base ** exp)
            print(f"{base}**{exp} = {base ** exp}")
        base += 1
    exp += 1

print(len(numbers))