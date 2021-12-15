# O(n) time | O(n) space - where n is the length of the input string
def runLengthEncoding(string):
	run_length_encoded = []
	prev_char = string[0]
	num_similar_char = 1
	for char in string[1:]:
		if char == prev_char:
			num_similar_char += 1
		else:
			run_length_encoded.append(encodeHelper(prev_char, num_similar_char))
			num_similar_char = 1
			prev_char = char		
	
	run_length_encoded.append(encodeHelper(string[-1], num_similar_char))
	
	return "".join(run_length_encoded)
	

def encodeHelper(char, num_similar_char):
	encoded_str = []
	
	num_whole_char = num_similar_char // 9
	remainder = num_similar_char % 9
	
	for i in range(num_whole_char):
		encoded_str.append(f"9{char}")
		
	if remainder > 0:
		encoded_str.append(f"{remainder}{char}")
		
	return "".join(encoded_str)
