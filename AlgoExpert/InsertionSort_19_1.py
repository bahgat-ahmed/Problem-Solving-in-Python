# O(n^2) time | O(1) space - where n it the length of the input array

def insertionSort(array):
    for i in range(1, len(array)):
	for j in reversed(range(i)):
		if array[j+1] < array[j]:
			array[j], array[j+1] = array[j+1], array[j]
		else:
			break
				
    return array
