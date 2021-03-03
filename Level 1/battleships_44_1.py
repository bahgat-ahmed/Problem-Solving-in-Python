import numpy as np

num_test_cases = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def is_valid_fn(ii, jj, nn, seen_, grid_, ship_len_):
    if ii >= 0 and jj >= 0 and ii < nn and jj < nn and seen_[ii][jj] == 0 and\
     (grid_[ii][jj] == 'x' or grid_[ii][jj] == '@') and (ship_len_+1 <= nn/2):
        return 1
    else:
        return 0


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
            ship_len = 0
            if (grid[i][j] == 'x') and (seen[i][j] == 0):
                seen[i][j] = 1
                alive_ships += 1
                ship_len += 1

                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]

                    if is_valid_fn(x, y, grid_dim, seen, grid, ship_len):
                        seen[x][y] = 1
                        ship_len += 1
                        enter_1, enter_2 = True, True
                        if abs(dx[k]):
                            for idx, m in enumerate(range(x+1, x + int(np.ceil(grid_dim/2) + 1)), 1):
                                if is_valid_fn(m, y, grid_dim, seen, grid,
                                   ship_len) and enter_1:
                                    seen[m][y] = 1
                                    ship_len += 1
                                else:
                                    enter_1 = False
                                if is_valid_fn(x-idx, y, grid_dim, seen, grid,
                                   ship_len) and enter_2:
                                    seen[x-idx][y] = 1
                                    ship_len += 1
                                else:
                                    enter_2 = False
                        else:
                            for idx, n in enumerate(range(y+1, y + int(np.ceil(grid_dim/2)) + 1), 1):
                                if is_valid_fn(x, n, grid_dim, seen, grid, ship_len) and enter_1:
                                    seen[x][n] = 1
                                    ship_len += 1
                                else:
                                    enter_1 = False
                                if is_valid_fn(x, y-idx, grid_dim, seen, grid, ship_len) and enter_2:
                                    seen[x][y-idx] = 1
                                    ship_len += 1
                                else:
                                    enter_2 = False
                        break

    output_print.append(f"Case {idxx+1}: {alive_ships}")

for output in output_print:
    print(output)
    
