# O(n) time | O(1) space - where n is the length of the input array
def firstDuplicateValue(array):
    for idx in range(len(array)):
		if array[abs(array[idx]) - 1] < 0:
			return abs(array[idx])
		array[abs(array[idx]) - 1] = - array[abs(array[idx]) - 1]
	return -1
