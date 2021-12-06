# O(n) time | O(1) space - where n is the length of the input string
def isPalindrome(string):
    if len(string) % 2 == 0:
		max_iter = len(string) // 2
	else:
		max_iter = (len(string) - 1) // 2

	for i in range(max_iter):
		if string[i] != string[len(string) - 1 - i]:
			return False
	return True
                