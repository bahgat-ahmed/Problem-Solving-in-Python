input(); coins = sorted(map(int, input().split())); sum_ = i = 0

while sum_ <= sum(coins): sum_ += coins.pop(); i += 1

print(i)
