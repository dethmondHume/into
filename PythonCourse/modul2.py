def convert_n_to_m(x, n, m):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # n != n
    if isinstance(x, str) or isinstance(x, int):
        for i in str(x).upper():
            j = n
            while j < len(alphabet):
                if alphabet[j] == i:
                    return False
                j += 1
    # first convert to decimal number
    if isinstance(x, str):
        x = int(x, n)
    elif isinstance(x, int) or isinstance(x, long):
        x = int(x)
        if x % 10 == n:
            return False
        else:
            x = int(x)
    else:
        return False
    # now convert decimal to 'to_base' base
    result = ''
    if m < 2:
        x = int(str(x), n)
        for i in range(x):
            result += '0'
    if result != '':
        return result
        
    
    if x < m:
        return str(alphabet[x])
    else:
        return str(convert_n_to_m(x // m, n, m) + alphabet[x % m])
