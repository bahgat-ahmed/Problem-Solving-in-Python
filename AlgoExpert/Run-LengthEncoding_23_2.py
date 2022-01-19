# O(n) time | O(n) space - where n is the length of the input string
def runLengthEncoding(string):
	# the input string is guaranteed to be non-empty
    encoded_string_characters = []
	current_run_length = 1
	previous_char = string[0]
	
	for current_char in string[1:]:
		if current_char != previous_char or current_run_length == 9:
			encoded_string_characters.append(f"{current_run_length}{previous_char}")
			current_run_length = 0
			previous_char = current_char
		
		current_run_length += 1
	# handle the last run
	encoded_string_characters.append(f"{current_run_length}{string[-1]}")
	
	return "".join(encoded_string_characters)
