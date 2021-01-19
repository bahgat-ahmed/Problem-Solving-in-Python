input_nums = list(map(int, input().split()))

best_options = [idx for idx in range(max(input_nums), 7)]

if len(best_options) == 0:
    probability_numerator = 0
    probability_denominator = 1
else:
    probability_numerator = len(best_options)

    if probability_numerator == 4:
        probability_numerator = 2
        probability_denominator = 3

    elif probability_numerator == 5:
        probability_denominator = 6

    else:
        probability_denominator = int(6/probability_numerator)
        probability_numerator = 1

print(f'{probability_numerator}/{probability_denominator}')
