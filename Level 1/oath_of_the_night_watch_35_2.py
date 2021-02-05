n = int(input()); stewards_strengths = list(map(int, input().split()))

print(max(0, n - stewards_strengths.count(max(stewards_strengths)) - stewards_strengths.count(min(stewards_strengths))))
