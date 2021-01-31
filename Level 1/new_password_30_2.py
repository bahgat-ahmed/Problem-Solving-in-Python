import string

pass_length, num_distinct = map(int, input().split())

print((string.ascii_lowercase[:num_distinct] * pass_length)[:pass_length])
