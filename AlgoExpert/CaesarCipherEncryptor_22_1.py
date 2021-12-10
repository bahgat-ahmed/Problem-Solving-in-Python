# O(n) time | O(n) space - where n is the length of the input string
def caesarCipherEncryptor(string, key):
	ciphered_string = []
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	for char in string:
		ciphered_char_idx = (alphabet.index(char) + key) % len(alphabet)
		ciphered_string.append(alphabet[ciphered_char_idx])
	
	return "".join(ciphered_string)
		
		
