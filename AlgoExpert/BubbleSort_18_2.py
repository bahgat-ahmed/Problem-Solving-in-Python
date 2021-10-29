# O(n^2) time | O(1) space - where n is the length of the input array
# Best: O(n) time | O(1) space - when input array is already sorted
def bubbleSort(array):
    is_sorted = False
	counter = 0
	while not is_sorted:
		is_sorted = True
		for i in range(len(array) - 1 - counter):
			if array[i + 1] < array[i]:
				array[i + 1], array[i] = array[i], array[i + 1]
				is_sorted = False
		counter += 1
	return array
