word = input().strip()

num_lowercase_chars, num_uppercase_chars = 0, 0

for char in word:
    if char.islower():
        num_lowercase_chars += 1
    else:
        num_uppercase_chars += 1

if num_uppercase_chars > num_lowercase_chars:
    print(word.upper())
else:
    print(word.lower())
