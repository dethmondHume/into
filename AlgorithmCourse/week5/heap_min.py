# build min heap
def build_min_heap(array):
	heap_size = len(array)
	mid = len(array) // 2 - 1
	for i in range(mid, -1, -1):
		min_heapify(array, i)
#restore heap		
def min_heapify(array, mid):
	l = mid * 2 + 1
	r = mid * 2 + 2
	if l < len(array) and array[l] < array[mid]:
		smallest = l
	else:
		smallest = mid
	if r < len(array) and array[r] < array[smallest]:
		smallest = r
	if smallest != mid:
		array[mid], array[smallest] = array[smallest], array[mid]
		min_heapify(array, smallest)