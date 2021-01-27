import math

num_cakes, oven_baking_time, num_simul_cakes, oven_build_time = list(map(int, input().split()))

# dividing all given cakes into the final number of groups such that they will fit into the furnace
num_groups = math.ceil(num_cakes/num_simul_cakes)

# first calculating the total time taken using two furnaces
# making two counters for the available times for each furnace
oven_1_available_time, oven_2_available_time = 0, oven_build_time

# looping over the groups, the cakes will be given to the earliest available furnace at that time
for i in range(num_groups):

    if oven_1_available_time <= oven_2_available_time: oven_1_available_time += oven_baking_time

    else: oven_2_available_time += oven_baking_time

two_furnaces_time = max(oven_1_available_time, oven_2_available_time)
# second calculating the total time taken using one furnace
one_furnace_time = num_groups*oven_baking_time

print("YES" if two_furnaces_time < one_furnace_time else "NO")
