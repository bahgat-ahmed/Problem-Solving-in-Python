num_coinst = int(input())

coins = list(map(int, input().split()))

sum_1, remaining_sum = 0, sum(coins)

coins.sort(reverse=True)

for idx, coin in enumerate(coins):
    sum_1 += coin
    remaining_sum -= coin

    if sum_1 > remaining_sum:
        break

print(idx + 1)
