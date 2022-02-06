# O(n+m) time | O(c)space | where n is the number of characters, m is the length of the document, and c is the
# number of unique characters in the character string

def generateDocument(characters, document):
    char_freq = get_freq_fn(characters)
	doc_freq = get_freq_fn(document)
	
	for key, value in doc_freq.items():
		if key in char_freq:
			if char_freq[key] < value:
				return False
		else:
			return False
    return True


def get_freq_fn(string):
	freq_dict = dict()
	for char in string:
		if char in freq_dict:
			freq_dict[char] += 1
		else:
			freq_dict[char] = 1
			
	return freq_dict
