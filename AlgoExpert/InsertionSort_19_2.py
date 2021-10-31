# O(n^2) time | O(1) space - where n it the length of the input array

def insertionSort(array):
    for i in range(1, len(array)):
		j = i - 1
		while j >= 0 and array[j] > array[j+1]:
			swap(j, array)
			j -= 1
	return array


def swap(j, array):
	array[j], array[j+1] = array[j+1], array[j]
	
