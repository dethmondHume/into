import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if a > 0:
    if b > 0:
        if c > 0:
            if a + b > c:
                if a + c > b:
                    if b + c > a:
                        print "triangle"
                    else:
                        print "not triangle"
                else:
                    print "not triangle"
            else:
                print "not triangle"
        else:
            print "not triangle"
    else:
        print "not triangle"
else:
    print "not triangle"



