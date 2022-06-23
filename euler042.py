import os

def wordvalue(word, dictionary):
    value = 0
    for l in range(len(word)):
        value += dictionary[word[l]]
    return value

# Create dictionary
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dictionary = {}
for l in range(len(alphabet)):
    dictionary[alphabet[l]] = l + 1



with open('p042_words.txt', 'r') as words:
    lst = str(words.read()).split(',')
    lst = [w.strip('"') for w in lst]

max_len = 0

for w in lst:
    if len(w) > max_len:
        max_len = len(w)

max_score = 26 * max_len

# find first triangle number greater than max_score

triangles = []
t = 1
while t < max_score:
    triangles.append(int(0.5 * t * (t + 1)))
    t += 1

counter = 0
for w in lst:
    if wordvalue(w, dictionary) in triangles:
        counter += 1

print(counter)
