# O(n) time | O(1) space - where n is the length of the input array
def findThreeLargestNumbers(array):
	three_largest_nums = [None, None, None]
	for num in array:
		update_three_largest(three_largest_nums, num)
	return three_largest_nums


def update_three_largest(three_largest_nums, num):
	if three_largest_nums[2] is None or num >= three_largest_nums[2]:
		shift_and_update(three_largest_nums, num, 2)
	elif three_largest_nums[1] is None or num >= three_largest_nums[1]:
		shift_and_update(three_largest_nums, num, 1)
	elif three_largest_nums[0] is None or num >= three_largest_nums[0]:
		shift_and_update(three_largest_nums, num, 0)
	

def shift_and_update(array, num, idx):
	for i in range(idx + 1):
		if i == idx:
			array[idx] = num
		else:
			array[i] = array[i + 1]
