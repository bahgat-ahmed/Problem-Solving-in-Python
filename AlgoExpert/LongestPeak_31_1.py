# O(n) time | O(1) space - where n is the length of the input array
def longestPeak(array):
	max_peak_len = 0
	for i in range(1, len(array) - 1):
		peak_len = get_peak_len(i, array)
		if peak_len > max_peak_len:
			max_peak_len = peak_len
			
	return max_peak_len
		
	
def get_peak_len(i, array):
	peak_len = 1
	left = i - 1
	current_num = i
	left_part = None
	while array[current_num] > array[left]:
		left_part = True
		peak_len += 1
		if left > 0:
			left -= 1
			current_num -= 1
		else:
			break
	if left_part:
		right = i + 1
		right_part = None
		current_num = i
		while array[current_num] > array[right]:
			right_part = True
			peak_len += 1
			if right < len(array) - 1:
				right += 1
				current_num += 1
			else:
				break
		if peak_len >= 3 and right_part:
			return peak_len
		return 0
	return 0
