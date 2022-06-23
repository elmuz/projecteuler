"""
import itertools
# a*0.01 + b*0.02 + c*0.05 + d*0.1 + e*0.2 + f*0.5 + g*1 + h*2 = 2


# Brute-force                                     
coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0] # 2£ can't be in any set
counter = 2 # 1*2£ + 2*1£
for i in range(3,30): #201
    
    comb = itertools.combinations_with_replacement(range(len(coins)), i)
    for j in comb:
        wallet = [coins[k] for k in list(j)]
        if sum(wallet) == 2.0:
            counter += 1
            print(wallet)

print(counter)
"""

"""
# Brute-force 2
def fill(resto, L_old):
    if resto >= 1:
        return L6(L_old)
    elif resto >= 0.5:
        return L5(L_old)
    elif resto >= 0.2:
        return L4(L_old)
    elif resto >= 0.1:
        return L3(L_old)
    elif resto >= 0.05:
        return L2(L_old)
    elif resto >= 0.02:
        return L1(L_old)
    else:
        return L0(L_old)

def L0(L_old): # 1cent
    return 0

def L1(L_old): # 2cent
    return 1

def L2(L_old, delta): # 5cent
    # Può contenere [0,1,2]*2cent
    counter = fill(delta)
    for i in range(3):
        if i == 0: # Usa solamente X*1cent
            counter += 1
        else:
            counter += i * fill(0.02) + fill(5.0 - i * 0.02)
    return counter

L0 = [(1, L1), (1, L1)] # 2£
L1 = [(L2
"""
"""
# Pallottoliere
b = [200, 0, 0, 0, 0, 0, 0, 0]

def a01(): # 1cent -> 2cent
    b[0] -= 2
    b[1] += 1

def a12(): # 2cent -> 5cent
    b[0] += 1
    b[1] -= 3
    b[2] += 1

def a23(): # 5cent -> 10cent
    b[2] -= 2
    b[3] += 1

def a34(): # 10cent -> 20cent
    b[3] -= 2
    b[4] += 1

def a45(): # 20cent -> 50cent
    b[0] += 10
    b[4] -= 3
    b[5] += 1

def a56(): # 50cent -> 1€
    b[5] -= 2
    b[6] += 1

def a67(): # 1€ -> 2€
    b[6] -= 2
    b[7] += 1

counter = 1

while b[0] > 0:
    a01()
    counter += 1
    while b[1] > 0:
        a12()
        counter += 1
        while b[2] > 0
"""
"""
import numpy as np
tagli = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0]

def totale(v):
    t = 0
    for i in range(len(v)):
        t += v[i] * tagli[i]
    return t

solutions = np.array([0,0,0,0,0,0,0,1])
counter = 1

def fork(vector):
    if totale(vector) > 2:
        #return
        print('no')
    elif totale(vector) == 2:
        #solutions = np.vstack((solutions, vector))
        print('soluzione')
        counter += 1
        #return
    else:
        for i in range(len(tagli) - 1):
            vector[i] += 1
            fork(vector)

fork(np.array([0,0,0,0,0,0,0]))

print(counter)
"""        

# Per ogni taglio 't' prova a comporre il residuo
# D = 2.00 - n_t * X_t, dove 't' sono i tagli superiori.
# Ad esempio prendo n_2 = [0,1,2,3,4] 50cent e provo a
# riempire il delta D = 2€ - n_1 * 1€ - n_2 * 0.5€ con
# i soli tagli inferiori.

counter = 1 # combinazioni di 1 * 2€
print([1,0,0,0,0,0,0,0])

for n1 in range(200 // 100 + 1): # prendo [0,1,2] 1€
    
    if 200 - n1 == 0:
        counter += 1 # caso di soli 1€
        break
    
    # In caso di 1*1€ posso prendere al massimo 2*50cent
    # cioè (2.0 - n1 * 1) / 0.5
    for n2 in range((200 - n1 * 100) // 50 + 1): # [0,..,4] 50cent

        if 200 - n1 * 100 - n2 * 50 == 0:
            counter += 1 # casi di soli [1€]50cent
            break

        for n3 in range((200 - n1 * 100  - n2 * 50) // 20 + 1): # [0,..,10] 20cent

            if 200 - n1 * 100 - n2 * 50 - n3 * 20 == 0:
                counter += 1 # casi di soli [1€,50c]20cent
                break

            for n4 in range((200 - n1 * 100 - n2 * 50 - n3 * 20) // 10 + 1): # [0,..,20] 10cent

                if 200 - n1 * 100 - n2 * 50 - n3 * 20 - n4 * 10 == 0:
                    counter += 1 # casi di soli [1€,50c,20c]10cent
                    break

                for n5 in range((200 - n1 * 100 - n2 * 50 - n3 * 20 - n4 * 10) // 5 + 1): # 5cent

                    if 200 - n1 * 100 - n2 * 50 - n3 * 20 - n4 * 10 - n5 * 5 == 0:
                        counter += 1 # casi di soli [1€,50c,20c,10c]5cent
                        break

                    for n6 in range((200 - n1 * 100 - n2 * 50 - n3 * 20 - n4 * 10 - n5 * 5) // 2 + 1): # 2cent
                        # Fissati i 2cent esiste una sola quantità di 1cent che somma a 2.00
                        counter += 1
                        cent = 200 - n1 * 100 - n2 * 50 - n3 * 20 - n4 * 10 - n5 * 5 - n6 * 2
                        print([0,n1,n2,n3,n4,n5,n6,cent])


print(counter)


