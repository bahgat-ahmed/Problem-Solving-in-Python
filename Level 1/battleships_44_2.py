import numpy as np

num_test_cases = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def search(ii, jj, nn, seen_, grid_):
    if ii >= 0 and jj >= 0 and ii < nn and jj < nn and seen_[ii][jj] == 0 and\
     (grid_[ii][jj] == 'x' or grid_[ii][jj] == '@'):
        seen_[ii][jj] = 1
        search(ii + 1, jj,  nn, seen_, grid_)
        search(ii - 1, jj,  nn, seen_, grid_)
        search(ii, jj + 1,  nn, seen_, grid_)
        search(ii, jj - 1,  nn, seen_, grid_)
    else:
        return


output_print = list()

for idxx in range(num_test_cases):
    grid_dim = int(input())
    grid = list()
    alive_ships = 0

    for _ in range(grid_dim):
        grid.append(list(input()))

    seen = np.zeros((grid_dim, grid_dim))

    for i in range(grid_dim):
        for j in range(grid_dim):
            if (grid[i][j] == 'x') and (seen[i][j] == 0):
                alive_ships += 1
                search(i, j, grid_dim, seen, grid)

    output_print.append(f"Case {idxx+1}: {alive_ships}")

for output in output_print:
    print(output)
