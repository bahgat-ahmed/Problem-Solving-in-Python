# O(n) time | O(1) space - where n is the length of the input string
def isPalindrome(string):
    left_idx = 0
	right_idx = len(string) - 1
	while left_idx < right_idx:
		if string[left_idx] != string[right_idx]:
			return False
		left_idx += 1
		right_idx -= 1
	return True
