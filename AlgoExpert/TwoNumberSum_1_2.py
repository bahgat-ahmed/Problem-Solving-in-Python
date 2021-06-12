# O(n) time | O(1) space
def twoNumberSum(array, targetSum):
    for num in array:
        other_num = (targetSum - num)
        # the second part in the if condition to avoid repeating the same
        # number
        if (other_num in array) and (num != other_num):
            return [num, targetSum - num]
    return []
