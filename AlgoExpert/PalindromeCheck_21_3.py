# recursion
# O(n) time | O(n) space - where n is the length of the input string
def isPalindrome(string, start_idx=0):
	last_idx = len(string) - 1 - start_idx
	return True if start_idx >= last_idx else string[start_idx] == string[last_idx]\
				and isPalindrome(string, start_idx + 1)

# using tail recursion
# O(n) time | (O(1) space with some compilers) - where n is the length of the input string
def isPalindrome(string, start_idx=0):
	last_idx = len(string) - 1 - start_idx
	if start_idx >= last_idx:
		return True
		
	if string[start_idx] != string[last_idx]:
		return False
	return isPalindrome(string, start_idx + 1)
