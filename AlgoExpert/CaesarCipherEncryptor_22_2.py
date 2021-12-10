# O(n) time | O(n) space - where n is the length of the input string
def caesarCipherEncryptor(string, key):
	ciphered_string = []
	new_key = key % 26
    for char in string:
		new_letter_code = ord(char) + new_key
		if new_letter_code <= 122:
			ciphered_string.append(chr(new_letter_code))
		else:
			ciphered_string.append(chr(96 + new_letter_code % 122))
	return "".join(ciphered_string)
