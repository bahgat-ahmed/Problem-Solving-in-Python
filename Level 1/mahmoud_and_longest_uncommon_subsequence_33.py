string_1, string_2 = input(), input()

print(-1 if string_1 == string_2 else max(len(string_1), len(string_2)))
