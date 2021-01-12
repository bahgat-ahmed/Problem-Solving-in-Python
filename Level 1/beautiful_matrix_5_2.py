# gettting the inputs
for i in range(5):
    row_i = list(map(int, input().split()))
    if 1 in row_i:
        row_pos = i
        col_pos = row_i.index(1)

if row_pos > 2:
    row_move = (row_pos - 2)
else:
    row_move = (2 - row_pos)

if col_pos > 2:
    col_move = (col_pos - 2)
else:
    col_move = (2 - col_pos)

min_no_moves = row_move + col_move

print(min_no_moves)
