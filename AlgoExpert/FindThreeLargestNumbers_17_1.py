from typing import Tuple


# O(n) time | O(1) space - where n is the length of the input array
def findThreeLargestNumbers(array):
	small, middle, large = sub_array_largest_3_fn(array[:3])
	
	for num in array[3:]:
		if num >= large:
			small = middle
			middle = large
			large = num
		elif num >= middle:
			small = middle
			middle = num
		elif num >= small:
			small = num
			
	return [small, middle, large]

		
def sub_array_largest_3_fn(sub_array: list) -> Tuple[int, int, int]:
	largest = max(sub_array)
	largest_idx = sub_array.index(largest)
	smallest = min(sub_array)
	smallest_idx = sub_array.index(smallest)
	for idx, _ in enumerate(sub_array):
		if (idx != largest_idx) and (idx != smallest_idx):
			middle_idx = idx
			break
	return smallest, sub_array[middle_idx], largest		