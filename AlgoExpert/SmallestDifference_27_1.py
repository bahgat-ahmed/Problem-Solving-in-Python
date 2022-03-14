# O(n x m) time | O(1) space - where n is the length of the first input array and m is
# the length of the second input array
def smallestDifference(array_one, array_two):
	array_one.sort()
	array_two.sort()
    array_one_num = array_one[0]
	array_two_num = array_two[0]
	min_diff = abs(array_one_num - array_two_num)
	
	for num_1 in array_one:
		entered = False
		for num_2 in array_two:
			if abs(num_1 - num_2) < min_diff:
				entered = True
				array_one_num = num_1
				array_two_num = num_2
				min_diff = abs(array_one_num - array_two_num)
			elif entered:
				break

	return [array_one_num, array_two_num]