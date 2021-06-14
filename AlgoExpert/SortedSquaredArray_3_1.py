# O(nlog(n)) time | O(n) space - where n is the length of the input array
def sortedSquaredArray(array):
    # create new array to avoid modifying the input array
    new_array = [a**2 for a in array]
    return sorted(new_array)
