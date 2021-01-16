no_of_stones = int(input())
stones_colors = input()

min_no_stones_to_remove = 0
compare_1_index = 0

if no_of_stones > 1:

    for i in range(no_of_stones - 1):
        # if the two consecutive stones are not the same, remove one of them
        if stones_colors[compare_1_index] == stones_colors[i+1]:
            min_no_stones_to_remove += 1

        compare_1_index = i + 1

print(min_no_stones_to_remove)
