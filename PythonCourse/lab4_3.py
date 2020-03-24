import sys


input_list = sys.argv[1]
k = 0
           
for i in input_list:
    if i == '(':
        k = k + 1
    else:
        k = k - 1

    if k < 0:
        break

if k == 0:
    print "YES"
else:
    print "NO"
