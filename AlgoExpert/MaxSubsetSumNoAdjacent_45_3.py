# O(n) time | O(1) space - where n is the length of the input array (cleaner code)
def maxSubsetSumNoAdjacent(array):
    current_max, previous_max = 0, 0
    for num in array:
        previous_max, current_max = current_max, max(current_max, previous_max + num)
    return current_max
