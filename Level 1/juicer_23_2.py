inputs = lambda: list(map(int, input().split()))

num_oranges, max_orange_size, max_overall_size = inputs()

orange_sizes = inputs()

overall_juice_size, num_empty_waste = 0, 0

for orange_size in orange_sizes:
    
    if orange_size <= max_orange_size:
        overall_juice_size += orange_size

    if overall_juice_size > max_overall_size:
        num_empty_waste += 1
        overall_juice_size = 0

print(num_empty_waste)
