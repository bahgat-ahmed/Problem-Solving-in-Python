# O(nlog(n)) time | O(1) space
def twoNumberSum(array, targetSum):
    # sort array in-place
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        current_sum = array[left] + array[right]
        if targetSum == current_sum:
            return [array[left], array[right]]
        elif targetSum > current_sum:
            left += 1
        else:
            # then targetSum < current_sum:
            right -= 1
    return []
