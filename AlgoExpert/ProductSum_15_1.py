# O(n) time | O(d) space - where n is the number of elements in the array,
# including "inner" arrays and their sub-elements, and d is the greatest depth
# of "inner" arrays in the input array
def productSum(array, depth=1):
    product_sum = 0
    for element in array:
        if type(element) is int:
	    product_sum += element
	else:
	    product_sum += productSum(element, depth + 1)

    return product_sum * depth
