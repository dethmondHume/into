import sys

min_number = sys.argv[1]
max_number = sys.argv[2]
amount = 0

str1 = ''
str2 = ''

for i in range(6 - len(min_number)):
    str1 = str1 + '0'
str1 = str1 + min_number
for i in range(6 - len(max_number)):
    str2 = str2 + '0'
str2 = str2 + max_number

str2_i = int(str2) + 1
str1_i = int(str1)

tmp = ''
for i in range(str1_i, str2_i):
    if (int(str1[0]) + int(str1[1]) + int(str1[2]) == int(str1[3]) + int(str1[4]) + int(str1[5])):
        amount = amount + 1
    str1 = str(int(str1) + 1)
    
    for i in range(6 - len(str1)):
        tmp = tmp + '0'
        
    tmp = tmp + str1
    str1 = tmp
    tmp = ''
        
print amount
