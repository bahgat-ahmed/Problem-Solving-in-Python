# iterative solution
# O(log(n)) time | O(1) space
def binarySearch(array, target):

	left = 0
	right = len(array) - 1
	
	while left <= right:
		
		middle = (left + right) // 2
		potential_match = array[middle]

		if target < potential_match:
			right = middle - 1
		elif target > potential_match:
			left = middle + 1
		else:
			return middle
		
	return -1
