# a function for getting string position in a matrix
def find(num, matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == num:
                return (i, j)

# gettting the inputs
matrix = []
for i in range(5):
    matrix.append(list(map(int, input().split())))

one_position = find(1, matrix)

if one_position[0] > 2:
    row_move = (one_position[0] - 2)
else:
    row_move = (2 - one_position[0])

if one_position[1] > 2:
    col_move = (one_position[1] - 2)
else:
    col_move = (2 - one_position[1])

min_no_moves = row_move + col_move

print(min_no_moves)
