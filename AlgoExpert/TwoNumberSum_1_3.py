# O(n) time | O(n) space
def twoNumberSum(array, targetSum):
    new_arr = []
    for num in array:
        other_num = targetSum - num
        if other_num in new_arr:
            return [other_num, num]
        else:
            new_arr.append(num)
    return []
