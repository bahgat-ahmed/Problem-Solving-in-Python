n = int(input())

print(('NO', 'YES')[len(set(input().lower())) == 26])
