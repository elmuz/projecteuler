sumos = 0
squareos = 0
for i in range(1,101):
    sumos += i**2
    squareos += i
squareos = squareos**2
print(squareos - sumos)

