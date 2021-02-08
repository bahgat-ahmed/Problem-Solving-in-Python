direction = input(); keyboard_chars = "qwertyuiopasdfghjkl;zxcvbnm,./"

for letter in input(): print(keyboard_chars[keyboard_chars.index(letter) + [1, -1][direction == "R"]], end="")
