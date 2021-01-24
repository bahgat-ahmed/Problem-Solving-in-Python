num_wires = int(input())
num_birds_per_wire = list(map(int, input().split()))

num_shots = int(input())

shots_positions = [list(map(int, input().split())) for i in range(num_shots)]

for shot_pos in shots_positions:

    x_pos, y_pos = shot_pos[0], shot_pos[1]
    x_pos, y_pos = x_pos - 1, y_pos - 1



    if x_pos > 0:
        num_birds_per_wire[x_pos - 1] += y_pos

    if x_pos < num_wires - 1:
        num_birds_per_wire[x_pos + 1] += (num_birds_per_wire[x_pos] - y_pos - 1)

    num_birds_per_wire[x_pos] = 0

for i in num_birds_per_wire:
    print(i)
