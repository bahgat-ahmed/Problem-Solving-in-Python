n = int(input())

stewards_strengths = list(map(int, input().split()))

num_to_support = 0

stewards_strengths_copy = sorted(set(stewards_strengths))

if len(stewards_strengths_copy) > 2:
    lowest_strength_count = stewards_strengths.count(stewards_strengths_copy[0])
    largest_strength_count = stewards_strengths.count(stewards_strengths_copy[-1])
    num_to_support = len(stewards_strengths) - lowest_strength_count - largest_strength_count

print(num_to_support)
