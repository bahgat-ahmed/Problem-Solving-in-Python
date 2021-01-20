from fractions import Fraction

input_nums = list(map(int, input().split()))

best_options = [idx for idx in range(max(input_nums), 7)]

num_best_options = 6 - max(input_nums) + 1

if num_best_options == 6:
    print("1/1")
else:
    print(str(Fraction(num_best_options, 6)))
