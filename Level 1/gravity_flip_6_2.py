no_of_cols = int(input())

columns = list(map(int, input().split()))[:no_of_cols]

columns.sort()
# (*columns) for printing the numbers in the list instead of including the list brackets and commas [ , , , ] in the print
print(*columns)
