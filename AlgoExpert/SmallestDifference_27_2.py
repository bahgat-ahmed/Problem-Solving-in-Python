# O(nlog(n) + mlog(m)) time | O(1) space - where n is the length of the first input array and m is
# the length of the second input array
def smallestDifference(array_one, array_two):
	array_one.sort()
	array_two.sort()
	
	array_one_idx = 0
	array_two_idx = 0
	min_diff = float('inf')
	
	while array_one_idx < len(array_one) and array_two_idx < len(array_two):
		
		first_num = array_one[array_one_idx]
		second_num = array_two[array_two_idx]
	
		if first_num < second_num:
			array_one_idx += 1
			current_diff = second_num - first_num
		elif first_num > second_num:
			array_two_idx += 1
			current_diff = first_num - second_num
		else:
			return [first_num, second_num]
			
		if current_diff < min_diff:
			min_diff = current_diff
			smallest_pair = [first_num, second_num]
		
	return smallest_pair