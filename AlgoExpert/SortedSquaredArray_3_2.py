# O(n) time | O(n) space - where n is the length of the input array
def sortedSquaredArray(array):
    sorted_array = [0 for _ in array]

    smaller_value_idx = 0
    larger_value_idx = len(array) - 1
    # start from the end of the sorted_array because I will compare the largest
    # values and insert them in the sorted_array accordingly
    for idx in reversed(range(len(array))):
        # the first and last input array elements are those competing against
        # the largest values if -ve values exist in the input array
        smaller_value = array[smaller_value_idx]
        larger_value = array[larger_value_idx]

        if abs(smaller_value) > abs(larger_value):
            sorted_array[idx] = smaller_value**2
            smaller_value_idx += 1
        else:
            sorted_array[idx] = larger_value**2
            larger_value_idx -= 1

    return sorted_array
