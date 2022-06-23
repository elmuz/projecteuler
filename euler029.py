t = []
for a in range(2,101):
    for b in range(2, 101):
        t.append(a**b)
t = set(t)
print(len(t))
