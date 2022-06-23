"""
I will use Berggren's theorem: https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples
"""
from collections import defaultdict

triangles = defaultdict(lambda: 0)
limit = 1500000
a = 3
b = 4
c = 5
to_check = [(a, b, c)]
while len(to_check) > 0:
    a, b, c = to_check.pop(0)
    if a + b + c > limit:
        continue
    triangles[a + b + c] += 1

    for k in range(2, limit // (a + b + c) + 1):
        triangles[k * (a + b + c)] += 1

    to_check.extend([
        (a - 2 * b + 2 * c, 2 * a - b + 2 * c, 2 * a - 2 * b + 3 * c),
        (a + 2 * b + 2 * c, 2 * a + b + 2 * c, 2 * a + 2 * b + 3 * c),
        (-a + 2 * b + 2 * c, -2 * a + b + 2 * c, -2 * a + 2 * b + 3 * c)
    ])

counter = 0
for t in triangles:
    if triangles[t] == 1:
        counter += 1
print(counter)