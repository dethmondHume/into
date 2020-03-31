handle = open("input__100.txt", "r")
data = handle.read()
handle.close()

tmp = data.split()
num = int(tmp[0])
array = tmp[1:num + 1]
COUNT = 0
print array

for i in range(len(array)):
    array[i] = int(array[i])


def partition(array, p, r):
    global COUNT
    x = array[r]
    i = p - 1
    for j in range(p, r):
        COUNT = COUNT + 1
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1

def quick_sort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quick_sort(array, p, q - 1)
        quick_sort(array, q + 1, r)

quick_sort(array, 0, num - 1)

print COUNT
print array
