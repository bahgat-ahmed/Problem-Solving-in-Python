# O(n) time | O(n) space - where n is the length of the input array
def maxSubsetSumNoAdjacent(array):
    if array:
        if len(array) <= 2:
            return max(array)
        else:
            max_sums = array[:]
            max_sums[1] = max(array[0], array[1])
            for i in range(2, len(array)):
                max_sums[i] = max(max_sums[i - 1], max_sums[i - 2] + array[i])
            return max_sums[-1]
    return 0
