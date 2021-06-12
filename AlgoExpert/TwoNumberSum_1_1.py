# O(n^2) time | O(1) space
def twoNumberSum(array, targetSum):
    for num_1 in array:
        for num_2 in array:
            if (num_1 != num_2) and (num_1 + num_2 == targetSum):
                return [num_1, num_2]
    return []
