with open("test_5_5.txt") as f:
    matrix = f.read()
    print matrix

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

begin = 0
end = 1
r = 1
while users > 0:
    print str(r) + ' array - ', input_data[begin + r : films + end]
    begin += films
    end += films + 1
    r += 1
    users -= 1

