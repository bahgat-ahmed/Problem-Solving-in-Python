sorted_nums = sorted(map(int, input().split('+')))

output_string = ''

if len(sorted_nums) > 0:
    for idx, num in enumerate(sorted_nums):
        if idx != len(sorted_nums) - 1:
            output_string += str(num) + '+'
        else:
            output_string += str(num)
else:
    output_string = sorted_nums[0]


print(output_string)
