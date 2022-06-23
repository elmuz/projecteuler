"""
Una volta che il resto della divisione si ripete
vuol dire che il periodo è concluso. Se il resto
eguaglia lo zero non esiste periodo. Non ha mai
senso testare divisori minori del periodo massimo
trovato.
"""
def longDivision(n):
    R = []
    resto = 1
    while resto != 0:
        resto = (resto * 10) % n
        if resto in R:
            return len(R) - R.index(resto)
        else:
            R.append(resto)
    return 0

longest = 0
d = 0
for n in range(999,1,-1):
    if longest >= n:
        break
    cycle = longDivision(n)
    if longest < cycle:
        longest = cycle
        d = n
print(str(d) + ' -> ' + str(longest))
