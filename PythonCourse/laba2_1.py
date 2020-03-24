import math
import sys

x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])

print 1 / (z * math.sqrt(2 * math.pi)) * math.exp(- math.pow( (x - y) , 2) / (2 * math.pow(z, 2)))