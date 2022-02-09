# O(n^2) time | O(n) space - where n is the length of the input array
def threeNumberSum(array, targetSum):
    array.sort()
	triplets = []
	for idx in range(len(array) - 2):
		left_idx = idx + 1
		right_idx = len(array) - 1

		while left_idx < right_idx:
			current_sum = array[idx] + array[left_idx] + array[right_idx]
			if current_sum < targetSum:
				left_idx += 1
			elif current_sum > targetSum:
				right_idx -= 1
			else:
				triplets.append([array[idx], array[left_idx], array[right_idx]])
				left_idx += 1
				right_idx -= 1
				
	return triplets
