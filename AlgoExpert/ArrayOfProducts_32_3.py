# O(n) time | O(n) space - where n is the length of the input array
def arrayOfProducts(array):
    array_of_products = [1] * len(array)
	
	prev_num = 1
	for i in range(1, len(array)):
		array_of_products[i] = array[i - 1] * prev_num
		prev_num *= array[i - 1]
	
	prev_num = 1
	for i in reversed(range(len(array) - 1)):
		array_of_products[i] = array[i + 1] * prev_num * array_of_products[i]
		prev_num *= array[i + 1]
	
	return array_of_products
