inputs = lambda: list(map(int, input().split()))

num_wires,  = inputs()

num_birds_per_wire = inputs()

num_shots = int(input())

for i in range(num_shots):

    x, y = inputs()
    x, y = x-1, y-1

    if x > 0:
        num_birds_per_wire[x - 1] += y

    if x < num_wires - 1:
        num_birds_per_wire[x + 1] += num_birds_per_wire[x] - y - 1

    num_birds_per_wire[x] = 0

print('\n'.join(map(str, num_birds_per_wire)))
