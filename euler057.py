from fractions import Fraction

e = Fraction(2 + 1/2)
f = Fraction(3, 2)

def expand_fraction(depth):

    a = Fraction(2 + 1/2)
    counter = 0
    
    for i in range(1, depth):
        
        a = Fraction(2 + 1/a)

        a_temp = a - 1
        if len(str(a_temp.numerator)) > len(str(a_temp.denominator)):
            counter += 1

    a -= 1
    return counter


print(expand_fraction(1001))
