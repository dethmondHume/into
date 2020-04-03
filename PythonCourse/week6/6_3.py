def saddle_point(matrix):
    cor1 = -1
    cor2 = -1
    exitFlag = False
    minimal = -1

    for i in range(len(matrix)):
        if len(matrix[i]) == 1:
            cor1 = 0
            cor2 = 0
            break
        
        for j in range(len(matrix[i]) - 1):
            if matrix[i][j] < matrix[i][j + 1]:
                minimal = matrix[i][j]
                cor1 = i
                cor2 = j
            elif matrix[i][j] > matrix[i][j + 1]:
                minimal = matrix[i][j + 1]
                cor1 = i
                cor2 = j + 1
            
        
                
        for k in range(len(matrix)):
            if k != cor1:
                if minimal <= matrix[k][cor2]:
                    if (i == len(matrix) - 1):
                        return False
                    else:
                        break
                elif k == len(matrix) - 1:
                    exitFlag = True         
            
        if exitFlag:
            break
                
 
    some_tupple = (cor1, cor2)
    
    return some_tupple

saddle_point([[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [11, 10, 9, 8, 7, 6, 5, 4, 3, 2], [12, 11, 10, 9, 8, 7, 6, 5, 4, 3], [13, 12, 11, 10, 9, 8, 7, 6, 5, 4], [14, 13, 12, 11, 10, 9, 8, 7, 6, 5], [15, 14, 13, 12, 11, 10, 9, 8, 7, 6], [16, 15, 14, 13, 12, 11, 10, 9, 8, 7], [17, 16, 15, 14, 13, 12, 11, 10, 9, 8], [18, 17, 16, 15, 14, 13, 12, 11, 10, 9], [19, 18, 17, 16, 15, 14, 13, 12, 11, 10]]) 
