# O(n) time | O(1) space - where n is the length of the input array
def isMonotonic(array):
    if len(array) <= 2:
		return True

	prev_num = array[0]
	decreased, increased = None, None
	
	for num in array[1:]:
		if num < prev_num:
			if increased:
				return False
			decreased = True
		elif num > prev_num:
			if decreased:
				return False
			increased = True
		prev_num = num
	
	return True
