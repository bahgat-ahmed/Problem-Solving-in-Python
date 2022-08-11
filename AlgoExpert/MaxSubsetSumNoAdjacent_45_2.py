# O(n) time | O(1) space - where n is the length of the input array
def maxSubsetSumNoAdjacent(array):
    if array:
        if len(array) <= 2:
            return max(array)
        else:
            first = array[0]
            second = max(array[0], array[1])
            for num in array[2:]:
                current = max(second, first + num)
                first, second = second, current
            return current
    return 0
