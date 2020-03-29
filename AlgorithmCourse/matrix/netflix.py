with open("gh1.txt") as f:
    matrix = f.read()
    

input_data = []
tmp = ''

###working code for vizualization lists favorites of users
##ERROR was when end file != ' ' or '\n'
for i in matrix:
    if i == ' ' or i == '\n':
        input_data.append(tmp)
        tmp = ''
    if i != ' ' and i != '\n':
        tmp += i

users = int(input_data[0])
films = int(input_data[1])
input_data = input_data[2:]

##begin = 0
##end = 1
##r = 1
##while users > 0:
##    if r == 1 or r == 618:
##        print str(r) + ' array - ', input_data[begin + r : films + end]
##    begin += films
##    end += films + 1
##    r += 1
##    users -= 1

def preference(user1, user2):
    begin = 0
    end = 1
    r = 1
    if user1 > user2:
        users = user1
    else:
        users = user2
    
    list_A = []
    list_B = []
    while users > 0:
        if r == user1:
            list_A = input_data[begin + r : films + end]
        elif r == user2:
            list_B = input_data[begin + r : films + end]
    
        begin += films
        end += films + 1
        r += 1
        users -= 1
     
    result = [0] * films
    f = 0
    for i in list_A:
        result[int(i) - 1] = list_B[f]
        f += 1
    
    count = 0
    k = 0
    j = 1
    while k < len(result):
        while j < len(result):
            
            if int(result[k]) > int(result[j]):
                count = count + 1
            j += 1
        k += 1
        j = k + 1
    return count
         
    
    
##print preference(2, 1)
##print preference(2, 3)
##print preference(2, 4)
##print preference(2, 5)
##print preference(452, 100)
##print preference(863, 29)
print preference(1, 618)
print preference(951, 178)
