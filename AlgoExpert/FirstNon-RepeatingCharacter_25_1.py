# O(n) time | O(1) space - where n is the length of the input string. The constant space is because the input
# string only has lowercase English-alphabet letters; thus, our hash table will never have more than 26 character
# frequencies

def firstNonRepeatingCharacter(string): 
	char_freq = {}
	for char in string:
		char_freq[char] = char_freq.get(char, 0) + 1
		
	for idx, char in enumerate(string):
		if char_freq[char] == 1:
			return idx
	return -1
