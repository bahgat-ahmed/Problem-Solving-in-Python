import numpy as np

num_test_cases = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def is_valid_fn(i, j, n, seen, grid, ship_len):
    if i > 0 and j > 0 and i < n and j < n and seen[i][j] == 0 and\
     grid[i][j] == 'x' and ship_len+1 <= n/2:
        seen[x][y] = 1
        return 1
    else:
        return 0

output_print = list()

for idx in range(num_test_cases):
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
                    if is_valid_fn(x, y, grid_dim, seen, grid, ship_len):
                        ship_len += 1
                        if dx[k]:
                            for m in range(x, x + int(np.ceil(grid_dim/2)) + 1):
                                if is_valid_fn(m+1, y, grid_dim, seen, grid, ship_len):
                                    ship_len += 1
                                if is_valid_fn(m-1, y, grid_dim, seen, grid, ship_len):
                                    ship_len += 1
                        else:
                            for n in range(y, y + int(np.ceil(grid_dim/2)) + 1):
                                if is_valid_fn(x, n+1, grid_dim, seen, grid, ship_len):
                                    ship_len += 1
                                if is_valid_fn(x, n-1, grid_dim, seen, grid, ship_len):
                                    ship_len += 1
                        break

    output_print.append(f"Case {idx+1}: {alive_ships}")

for output in output_print:
    print(output)
