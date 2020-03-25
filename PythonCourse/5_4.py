def file_search(folder, filename):

    result = ''
    for i in range(len(folder)):
        if folder[i] == filename:
            result = folder[0] + '/' + folder[i]
            
        for j in range(len(folder[i])):
            if folder[i][j] == filename:
                result = folder[0] + '/' + folder[i][0] + '/' + folder[i][j]
                
            for k in range(len(folder[i][j])):
                if folder[i][j][k] == filename:
                    result = folder[0] + '/' + folder[i][0] + '/' + folder[i][j][0] + '/' + folder[i][j][k]
                    
                for p in range(len(folder[i][j][k])):
                    if folder[i][j][k][p] == filename:
                        result = folder[0] + '/' + folder[i][0] + '/' + folder[i][j][0] + '/' + folder[i][j][k][0] + '/' + folder[i][j][k][p]

                    for o in range(len(folder[i][j][k][p])):
                        if folder[i][j][k][p][o] == filename:
                            result = folder[0] + '/' + folder[i][0] + '/' + folder[i][j][0] + '/' + folder[i][j][k][0] + '/' + folder[i][j][k][p][0] + '/' + folder[i][j][k][p][o]
                            
                        for r in range(len(folder[i][j][k][p][o])):
                            if folder[i][j][k][p][o][r] == filename:
                                result = folder[0] + '/' + folder[i][0] + '/' + folder[i][j][0] + '/' + folder[i][j][k][0] + '/' + folder[i][j][k][p][0] + '/' + folder[i][j][k][p][o][0] + '/' + folder[i][j][k][p][o][r]
                               
    if len(result) > 0:
        return result
    else:
        return False
                        
file_search(['/tmp', ['1', ['2', ['3', ['4', ['5', 'key1', 'key2', 'key3']]]]]], 'key3')
