def karaccuba(x, y):
    str_x = str(x)
    str_y = str(y)
    a = int(str_x[0 : len(str_x) / 2 + len(str_x) % 2])
    b = int(str_x[len(str_x) / 2 + len(str_x) % 2 : len(str_x)])
    c = int(str_y[0 : len(str_y) / 2 + len(str_y) % 2])
    d = int(str_y[len(str_y) / 2 + len(str_y) % 2 : len(str_y)])
    ac = a * c
    bd = b * d
    mid = (a + b) * (c + d) - ac - bd
    return 10 ** (len(str_x)) * ac + 10 ** (len(str_x) / 2) * mid + bd
    
#recursion metod
def karacuba(x, y):
    str_x = str(x)
    str_y = str(y)
    if len(str_x) > 1:
        a = int(str_x[0 : len(str_x) / 2 + len(str_x) % 2])
        b = int(str_x[len(str_x) / 2 + len(str_x) % 2 : len(str_x)])
    else:
        a = 0
        b = int(str_x)
    if len(str_y) > 1:
        c = int(str_y[0 : len(str_y) / 2 + len(str_y) % 2])
        d = int(str_y[len(str_y) / 2 + len(str_y) % 2 : len(str_y)])
    else:
        c = 0
        d = int(str_y)
    mid = (a + b) * (c + d) - a * c - b * d
    
    if len(str_x) > 1 or len(str_y) > 1:
        return karacuba(a + b, c + d) - karacuba(a, c) - karacuba(b, d)
    else:
        return 0
    
print karacuba(1234,
               5678)
"""print karacuba(1685287499328328297814655639278583667919355849391453456921116729,
               7114192848577754587969744626558571536728983167954552999895348492)
"""
