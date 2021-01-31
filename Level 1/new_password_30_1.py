import string

pass_length, num_distinct = map(int, input().split())

used_chars = string.ascii_lowercase[:num_distinct]

password = ''

idx = 0
for i in range(pass_length):
    if idx == len(used_chars):
        idx = 0
    password += used_chars[idx]
    idx += 1

print(password)
