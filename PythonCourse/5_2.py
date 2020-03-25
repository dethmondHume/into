def counter(a, b):
    a = list(set(str(a)))
    b = list(set(str(b)))
    count = 0
    i = 0
    
    while len(a):
        tmp = list(b)
        
        while len(tmp):
            
            if tmp[i] == a[i]:
                count = count + 1
                break
            else:
                del tmp[i]
        del a[i]
           
    return count

 
