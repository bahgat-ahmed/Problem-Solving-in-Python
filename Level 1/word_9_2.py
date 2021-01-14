word = input().strip()

num_lowercase_chars = sum(map(str.islower, word))
num_uppercase_chars = sum(map(str.isupper, word))

if num_uppercase_chars > num_lowercase_chars:
    print(word.upper())
else:
    print(word.lower())
