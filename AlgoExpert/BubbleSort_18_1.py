# O(n^2) time | O(1) space - where n is the length of the input array
# Best: O(n) time | O(1) space - when input array is already sorted
def bubbleSort(array):
    for i in range(len(array)):
		swap_happened = False
		for j in range(len(array) - 1 - i):
			if array[j+1] < array[j]:
				temp = array[j]
				array[j] = array[j+1]
				array[j+1] = temp
				swap_happened = True
		if swap_happened is False:
			break
				
	return array