# O(n) time | O(1) space - where n is the length of the input array
def firstDuplicateValue(array):
    for num in array:
		abs_value = abs(num)
		if array[abs_value - 1] < 0:
			return abs_value
		array[abs_value - 1] *= -1
	return -1
