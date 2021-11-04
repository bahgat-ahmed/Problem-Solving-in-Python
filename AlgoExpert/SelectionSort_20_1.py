# O(n^2) time | O(1) space - where n is the length of the input array
def selectionSort(array):
    for i in range(len(array)):
	smallest = i
	is_sorted = True
	for j in range(i + 1, len(array)):
		if array[smallest] > array[j]:
			smallest = j
			is_sorted = False
	if is_sorted is False:
		array[smallest], array[i] = array[i], array[smallest]

    return array
