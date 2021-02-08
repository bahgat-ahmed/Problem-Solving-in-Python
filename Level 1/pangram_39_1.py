import string

num_char = int(input())
string_ = input().lower()

all_letters = string.ascii_lowercase

if num_char >= len(all_letters):

    is_pangram = True

    for letter in all_letters:

        if letter not in string_:
            is_pangram = False

    print('YES') if is_pangram else print('NO')

else:
    print('NO')
