import sys

n = int(sys.argv[1])
fib = 0
prev1 = 0
prev2 = 1

if n == 1:
    print 1
else:
    for i in range(n - 1):
        fib = prev1 + prev2
        prev1 = prev2
        prev2 = fib
    print fib

