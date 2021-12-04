# O(n) time | O(n) space - where n is the length of the input string
def isPalindrome(string):
    if string == string[::-1]:
		return True
	else:
		return False
