#create new heap
def build_max_heap(array):
	heap_size = len(array)
	mid = len(array) // 2 - 1
	for i in range(mid, -1, -1):
		max_heapify(array, i)

#restoration properties of heap		
def max_heapify(array, mid):
	l = mid * 2 + 1
	r = mid * 2 + 2
	if l < len(array) and array[l] > array[mid]:
		largest = l
	else:
		largest = mid
	if r < len(array) and array[r] > array[largest]:
		largest = r
	if largest != mid:
		array[mid], array[largest] = array[largest], array[mid]
		max_heapify(array, largest)