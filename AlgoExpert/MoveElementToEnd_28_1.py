# O(n) time | O(1) space - where n is the length of the input array
def moveElementToEnd(array, toMove):
    for num in array:
		if num == toMove:
			array.remove(num)
			array.append(num)
	
	return array
