from heap_max import *
from heap_min import *

###shitcode for balanced max and min heaps

with open('ex42.txt', 'r') as input:
	data = input.read()

data = data.split()
length = data[0]
data = data[1:]
for i in range(len(data)):
	data[i] = int(data[i])
print(data)

heap_max = []
heap_min = []
for i in data:
	if heap_min == []:
		heap_min.append(i)
		continue
	if i < heap_min[0]:
		if len(heap_min) < len(heap_max):
			tmp = heap_max[0]
			heap_max[0] = i
			heap_min.append(tmp)
		else:
			heap_max.append(i)
	elif i > heap_min[0]:
		if len(heap_min) > len(heap_max):
			tmp = heap_min[0]
			heap_min[0] = i
			heap_max.append(tmp)
		else:
			heap_min.append(i)

	if heap_max != []:
		build_max_heap(heap_max)
	build_min_heap(heap_min)
	
	#result on iteration
	if data.index(i) + 1 == 2015:
		print(data.index(i) + 1)
		print(heap_max)
		print(heap_min, '\n')