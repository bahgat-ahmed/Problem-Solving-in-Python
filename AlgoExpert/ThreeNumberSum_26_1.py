# O(n^2) time | O(n) space - where n is the length of the input array
def threeNumberSum(array, targetSum):
    array.sort()
	triplets = []
	for num in array:
		left_idx = 0
		right_idx = len(array) - 2
		array_copy = array.copy()
		array_copy.remove(num)
		while left_idx < right_idx:
			current_sum = num + array_copy[left_idx] + array_copy[right_idx]
			if current_sum < targetSum:
				left_idx += 1
			elif current_sum > targetSum:
				right_idx -= 1
			else:
				triplet = sorted([num, array_copy[left_idx], array_copy[right_idx]])
				if triplet not in triplets:
					triplets.append(triplet)
				left_idx += 1
				right_idx -= 1

				
	return triplets
