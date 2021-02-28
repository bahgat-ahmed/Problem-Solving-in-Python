import numpy as np

num_test_cases = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def is_valid_fn(i, j, n):
    return i > 0 and j > 0 and i < n and j < n


for _ in range(num_test_cases):
    grid_dim = int(input())
    grid = list()
    alive_ships = 0
    ship_len = 0

    for _ in range(grid_dim):
        grid.append(list(input()))

    seen = np.zeros((grid_dim, grid_dim))

    for i in range(grid_dim):
        for j in range(grid_dim):
            if seen[i][j] == 0 and grid[i][j] == 'x':
                alive_ships += 1
                ship_len += 1
                seen[i][j] = 1

                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if is_valid_fn(x, y, grid_dim):
                        if seen[x][y] == 0 and grid[x][y] == 'x':
                            ship_len += 1
                            seen[x][y] = 1
