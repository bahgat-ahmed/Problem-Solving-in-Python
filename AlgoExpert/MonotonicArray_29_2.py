# O(n) time | O(1) space - where n is the length of the input array
def isMonotonic(array):
    is_non_increasing = True
	is_non_decreasing = True
	
	for i in range(1, len(array)):
		if array[i] < array[i - 1]:
			is_non_decreasing = False
		elif array[i] > array[i - 1]:
			is_non_increasing = False
		
	return is_non_increasing or is_non_decreasing
