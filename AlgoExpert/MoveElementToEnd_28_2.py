# O(n) time | O(1) space - where n is the length of the input array
def moveElementToEnd(array, toMove):
    left_idx = 0
	right_idx = len(array) - 1
	
	while left_idx < right_idx:
		if array[right_idx] == toMove:
			right_idx -= 1
		elif array[left_idx] == toMove:
			temp = array[left_idx]
			array[left_idx] = array[right_idx]
			array[right_idx] = temp
		else:
			left_idx += 1
			
	return array
				
			
