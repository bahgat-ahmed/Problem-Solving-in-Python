# O(nd) time | O(n) space - where n is the target amount and d is the number of coin denominations
def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for _ in range(n + 1)]
    ways[0] = 1

    for denom in denoms:
        for amount in range(denom, n + 1):
            ways[amount] += ways[amount - denom]
    return ways[n]
