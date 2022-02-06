# O(n+m) time | O(c)space | where n is the number of characters, m is the length of the document, and c is the
# number of unique characters in the character string

def generateDocument(characters, document):
	char_freq = dict()
	for char in characters:
		if char not in char_freq:
			char_freq[char] = 0
		char_freq[char] += 1
		
	for char in document:
		if char not in char_freq or char_freq[char] == 0:
			return False
		
		char_freq[char] -= 1
		
	return True
		
