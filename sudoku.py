def make_sudoku(size):
    result = [range(1, size**2 + 1)]
    for i in range(size - 1):
        tmp = []
        s = size
        for j in range(size**2):
            if s < size**2:
                tmp.append(result[i][s])
            else:
                s = 0
                tmp.append(result[i][s])
            s += 1
        result.append(tmp)
    for i in range(size**2 - size):
        tmp = []
        s = size - 1
        for j in range(size**2):
            if s < size**2:
                tmp.append(result[i][s])
            else:
                s = 0
                tmp.append(result[i][s])
            s += 1
        result.append(tmp)
        
    return result

print make_sudoku(3)
