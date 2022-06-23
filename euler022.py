reader = open('p022_names.txt','r') 
text = reader.read()
reader.close()

names = list(text.replace('"','').split(','))
names.sort()

a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

total = 0

for i in range(len(names)):
    score_letters = 0
    for letter in names[i]:
        score_letters += 1 + a.index(letter)
    total += (i + 1) * score_letters

print(total)
