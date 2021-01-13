no_of_cols = int(input())

columns = map(int, input().split())

# only getting the number of inputs obtained
columns = [col for idx, col in enumerate(columns) if idx < no_of_cols]
# (*sorted) for printing the numbers in the list instead of including the list brackets and commas [ , , , ] in the print
print(*sorted(columns))
