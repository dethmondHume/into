def make_sudoku(size):
    result = [range(1, size**2 + 1)]
    tmp = []
    value = 1
    
    y = 0 
    for i in range(size**2):
        while y < size**2:
            if result[0][y] == value or value in tmp:
                value += 1
            else:
                tmp.append(value)
                y += 1
                value = 1
    result.append(tmp)            
    tmp = []
    y = 0
    for i in range(size**2):
        while y < size**2:
            if result[1][y] == value or value in tmp:
                value += 1
            else:
                tmp.append(value)
                y += 1
                value = 1
    result.append(tmp)
    tmp = []
    y = 0
    for i in range(size**2):
        while y < size**2:
            if result[2][y] == value or value in tmp:
                value += 1
            else:
                tmp.append(value)
                y += 1
                value = 1    
    result.append(tmp)
    
    return result


print make_sudoku(2) # [[1,2,3,4],[3,4,1,2],[2,1,4,3],[4,3,2,1]]

