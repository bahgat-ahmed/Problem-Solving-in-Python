# gettting the inputs
for i in range(5):
    row_i = list(map(int, input().split()))
    if 1 in row_i:
        row_pos = i
        col_pos = row_i.index(1)

min_no_moves = abs(2 - row_pos) + abs(2 - col_pos)

print(min_no_moves)
