# O(n) time | O(1) space - where n is the length of the input array
def findThreeLargestNumbers(array):
	small, middle, large = None, None, None
	
	for num in array:
		if large is None or num >= large:
			small = middle
			middle = large
			large = num
		elif middle is None or num >= middle:
			small = middle
			middle = num
		elif small is None or num >= small:
			small = num
			
	return [small, middle, large]
