def find_fraction(summ):
    if summ < 3:
        return False
    if summ%2 != 0:
        a = summ/2
    else:
        a = summ/2 - 1
    b = summ - a
    flag = True
    while flag:
        if b % a == 0:
            break
        if a % (b % a) != 0 or (b % a) == 1:
            flag = False
        else:
            a = a - 1
            b = b + 1
            
    return (a, b)
    
    
print find_fraction(2) # False
print find_fraction(3) # (1, 2)
print find_fraction(10) # (3, 7)
print find_fraction(62) # (29, 33)
print find_fraction(150000001) # (75000000, 75000001)
