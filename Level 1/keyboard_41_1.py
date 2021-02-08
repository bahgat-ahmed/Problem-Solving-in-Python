direction = input()

wrong_message = input()

keyboard_chars = "qwertyuiopasdfghjkl;zxcvbnm,./"

correct_message = ""

for letter in wrong_message:
    if direction == "R":
        correct_message += keyboard_chars[keyboard_chars.index(letter) - 1]
    elif direction == "L":
        correct_message += keyboard_chars[keyboard_chars.index(letter) + 1]

print(correct_message)        
