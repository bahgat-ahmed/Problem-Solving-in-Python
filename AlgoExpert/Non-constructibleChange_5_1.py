# O(nlog(n)) time | O(1) space - where n is number of coins
def nonConstructibleChange(coins):
    coins.sort()
    # the minimum change that could be created
    min_change = 0

    for coin in coins:

        if coin > (min_change + 1):
            return min_change + 1

        min_change += coin

    return min_change + 1
