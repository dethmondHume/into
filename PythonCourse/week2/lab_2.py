import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

if x == 1:  la = "la"
else:       la = "la" + (x - 1)* "-la"

if y == 1:  cuplet = la
else:       cuplet = y * (" " + la)

if z == 1:  end = "!"
else:       end = "."

print "Everybody sing a song:" + cuplet + end
