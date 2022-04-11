# O(n) time | O(n) space - where n is the length of the input array
def firstDuplicateValue(array):
    new_array = set()
	for num in array:
		if num in new_array:
			return num
		new_array.add(num)
	return -1
